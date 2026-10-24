import scrapy

class housingscraperItem(scrapy.Item):
    flat=scrapy.Field()
    price=scrapy.Field()
    builtup_area=scrapy.Field()
    status=scrapy.Field()







