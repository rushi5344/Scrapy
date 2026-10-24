import scrapy
from ..items import AmazonScraperItem


class AmazonSpider(scrapy.Spider):
    name = "amazon-bot"
    count=1

    start_urls = [
        "https://www.amazon.com/s?k=headphones&page=1&crid=C86FHRIOZTAY&qid=1785674473&sprefix=%2Caps%2C288&xpid=XBkZTBYc0rebN&ref=sr_pg_2"
    ]

    custom_settings = {
        "USER_AGENT": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/150.0.0.0 Safari/537.36"
        )
    }

    def parse(self, response):

        products = response.css(
            'div[data-component-type="s-search-result"]'
        )

        for product_data in products:
            product = AmazonScraperItem()

            product["p_name"] = product_data.css(
                ' a h2 span::text'
            ).get()

            product["review"] = product_data.css(
                'a[aria-label$="ratings"] span::text'
            ).get()

            product["rating"] = product_data.css(
                'div[data-cy="reviews-block"] '
                'span.a-size-small.a-color-base[aria-hidden="true"]::text'
            ).get()

            product["price"] = product_data.css(
                'span.a-price span.a-offscreen::text'
            ).get()

            yield product
        AmazonSpider.count+=1
        next_page=response.css("a.s-pagination-next::attr(href)").get()
        print(next_page)
        if AmazonSpider.count<10:
            yield response.follow(next_page, callback=self.parse)
