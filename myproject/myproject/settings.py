

BOT_NAME = "myproject"

SPIDER_MODULES = ["myproject.spiders"]
NEWSPIDER_MODULE = "myproject.spiders"

SCRAPEOPS_API_KEY='337b6475-6238-4419-9851-9281d94d8cca'
SCRAPEOPS_PROXY_ENABLED=True
DOWNLOADER_MIDDLEWARES = {
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

ADDONS = {}




# Obey robots.txt rules
ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1


FEED_EXPORT_ENCODING = "utf-8"
