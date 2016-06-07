"""docstring here."""
from archi_scraper.spiders.archi_spider import ArchiSpider
import logging
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy import signals
from scrapy.utils.log import configure_logging
from twisted.internet import reactor


def spider_closing(spider):
    """docstring here."""
    logger.msg("Closing reactor", level=logger.INFO)
    reactor.stop()

configure_logging(install_root_handler=False)
logging.basicConfig(filemode='w')
logger = logging.getLogger()
logger.start(loglevel=logger.DEBUG)
settings = Settings()
crawler = CrawlerProcess(settings)
crawler.signals.connect(spider_closing, signal=signals.spider_closed)
crawler.configure()
crawler.crawl(ArchiSpider())
crawler.start()
reactor.run()
