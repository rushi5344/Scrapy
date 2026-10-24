import scrapy
from ..items import housingscraperItem


class housingscraper(scrapy.Spider):
    name = "housing-bot"
    count=1
    start_urls = ["https://housing.com/in/buy/thane/?page=1"]

    def parse(self, response):
        cards = response.css('article[data-testid="card-container"]')

        for card in cards:
            flat = " ".join(
                card.css("h2.title-style::text").getall()
            ).strip()

            price = card.css(
                'div[data-q="price"]::text'
            ).get()

            builtup_area = card.css(
                'div[data-q="builtup-area"] div::text'
            ).get()

            status = card.css(
                'div[data-q="property-detail"] div::text'
            ).get()

            # Skip this card if any field is missing
            if not all([flat, price, builtup_area, status]):
                continue

            product = housingscraperItem()

            product["flat"] = flat
            product["price"] = price.strip()
            product["builtup_area"] = builtup_area.strip(  )
            product["status"] = status.strip()

            yield product

        housingscraper.count+=1
        next_page ="https://housing.com/in/buy/thane/?page="+str(housingscraper.count)
        print(next_page)
        if housingscraper.count<6:
            yield response.follow(next_page,callback=self.parse)
