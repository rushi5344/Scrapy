BOT_NAME = "myproject"

SPIDER_MODULES = ["myproject.spiders"]
NEWSPIDER_MODULE = "myproject.spiders"

SCRAPEOPS_API_KEY='8a2561f7-f399-4508-a963-c802a311ca81'

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
