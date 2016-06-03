"""docstring here."""
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join
from scrapy.loader.processors import MapCompose
from scrapy import Request
from scrapy import Selector
from scrapy.spiders import Spider

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
        base_url = response.url

        for page in range(1, 1211):
            if page > 1:
                url = base_url + '/' + str(page)
            else:
                url = base_url
            yield Request(url, callback=self.parse_page)

    def parse_page(self, response):
        """docstring here."""
        selector = Selector(response)

        for archi in selector.xpath(self.archi_xpath):
            loader = ItemLoader(ArchiItem(), selector=archi)
            loader.default_input_processor = MapCompose(unicode.strip, unicode.upper)
            loader.default_output_processor = Join()

            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)

            yield loader.load_item()
