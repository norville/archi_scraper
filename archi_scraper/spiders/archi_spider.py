"""docstring here."""
from scrapy.contrib.loader.processor import Join
from scrapy.contrib.loader.processor import MapCompose
from scrapy.contrib.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import Spider

from archi_scraper.items import ArchiItem


class ArchiSpider(Spider):
    """docstring here."""

    name = 'archi_spider'
    allowed_domains = ['ordinearchitetti.mi.it']
    start_urls = ['http://www.ordinearchitetti.mi.it/it/ordine/albo']
    archi_xpath = '//*[@id="wraparchialbo"]/div'
    item_fields = {
        'name': './/a/h3/text()',
        'surname': './/a/h3/strong/text()',
        'sid': './/p[1]/span[text()="cod. fisc."]/following-sibling::text()[1]',
        'address': './/p[1]/span[text()="indirizzo"]/following-sibling::text()[1]'
    }

    def parse(self, response):
        """docstring here."""
        selector = HtmlXPathSelector(response)

        for archi in selector.select(self.archi_xpath):
            loader = XPathItemLoader(ArchiItem, selector=archi)
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
