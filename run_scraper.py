"""docstring here."""
from archi_scraper.spiders import ArchiSpider
from scrapy.crawler import CrawlerProcess


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(ArchiSpider)
process.start()
