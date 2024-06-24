import scrapy


class JokeItem(scrapy.Item):
    text = scrapy.Field()
