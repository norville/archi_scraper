from scrapy import Item, Field


class ArchItem(Item):
    name = Field()
    surname = Field()
    sid = Field()
    address = Field()
