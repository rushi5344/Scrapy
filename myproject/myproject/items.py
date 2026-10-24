import scrapy


class AmazonScraperItem(scrapy.Item):
    p_name = scrapy.Field()
    review = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()










