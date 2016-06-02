"""docstring here."""
from scrapy import Field
from scrapy import Item


class ArchiItem(Item):
    """docstring here."""

    name = Field()
    surname = Field()
    sid = Field()
    address = Field()
    zip_code = Field()
    city = Field()
