import scrapy
from ..items import LinkedinScrapperItem


class LinkedinSpider(scrapy.Spider):
    name = "linkedin-bot"
    count = 25

    start_urls = [
        "https://www.linkedin.com/jobs/search/?currentJobId=4454814946&keywords=data%20analyst&origin=SUGGESTION&start=0"
    ]

    def parse(self, response):

        cards = response.css("div.job-card-container")

        for card in cards:

            role = card.css(
                "a.job-card-list__title--link strong::text"
            ).get()

            company = card.css(
                "span.pkXTSOjuybKaxMNVefkdwtUQOqEFHJfJW::text"
            ).get()

            location = card.css(
                "div.artdeco-entity-lockup__caption "
                "ul.job-card-container__metadata-wrapper "
                "li span[dir='ltr']::text"
            ).get()

            product = LinkedinScrapperItem()

            product["role"] = role
            product["company"] = company
            product["location"] = location

            yield product

        self.count += 1

        next_page = (
            "https://www.linkedin.com/jobs/search/"
            "?currentJobId=4462202033"
            "&keywords=data%20analyst"
            "&origin=SUGGESTION"
            "&start=" + str(self.count)
        )

        print(next_page)

        if self.count < 7:
            yield response.follow(
                next_page,
                callback=self.parse
            )