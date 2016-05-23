from scrapy import Item, Field


class ArchiItem(Item):
    name = Field()
    surname = Field()
    sid = Field()
    address = Field()
    zip_code = Field()
    city = Field()
