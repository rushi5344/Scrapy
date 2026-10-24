import scrapy


class PharmEasy(scrapy.Spider):
    name = "pharmeasy"
    handle_httpstatus_all = True

    base_url = "https://pharmeasy.in/api/otc/getCategoryProducts?categoryId=9297&page="

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "accept": "application/json, text/plain, */*",
        "referer": "https://pharmeasy.in/",
    }

    def start_requests(self):
        # Start at page 1
        yield scrapy.Request(
            url=self.base_url + "1",
            headers=self.headers,
            callback=self.parse,
            meta={"page": 1},
        )

    def parse(self, response):
        if response.status != 200:
            return

        data = response.json()
        products = data.get("data", {}).get("products", [])

        # 1. Yield products from the current page
        for product in products:
            yield {
                "name": product.get("name"),
                "slug": product.get("slug"),
                "manufacturer": product.get("manufacturer"),
                "price": product.get("salePriceDecimal"),
                "availability": product.get("productAvailabilityFlags", {}).get("isAvailable"),
                "images": product.get("images"),
            }

        # 2. Pagination: check if products exist, then request next page
        if products:
            current_page = response.meta["page"]
            next_page_num = current_page + 1

            # Limit total pages if needed (e.g., stop at page 10)
            if next_page_num <= 10:
                yield scrapy.Request(
                    url=self.base_url + str(next_page_num),
                    headers=self.headers,
                    callback=self.parse,
                    meta={"page": next_page_num},
                )

