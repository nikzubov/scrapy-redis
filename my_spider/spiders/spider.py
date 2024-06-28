from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from my_spider.items import JokeItem


class MainSpider(CrawlSpider):
    """Базовый паук. Переходит по ссылкам категорий
    и страниц, забирает текст из 'holder-body' объектов"""
    name = "main_spider"
    allowed_domains = ["anekdoty.ru"]
    start_urls = ["https://anekdoty.ru"]

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths='//ul[@class="list"]/li/span/a'),
            callback="parse_item",
            follow=True),
    )

    def parse_item(self, response):
        jokes = response.xpath('//ul[@class="item-list"]/li')
        for joke in jokes:
            item = JokeItem()
            item['text'] = joke.xpath('string(.//div[@class="holder"]/div[@class="holder-body"])').get()
            yield item

        pagination_next = response.css('.next a')
        if pagination_next:
            yield from response.follow_all(pagination_next, self.parse_item)
