from redis import Redis
from twisted.internet.threads import deferToThread

from my_spider.config import settings


class RedisPipeline:
    key = '%(spider)s:items'

    def open_spider(
        self,
        spider,
    ):
        self.client = Redis(password=settings.R_PASSWORD)

    def process_item(
        self,
        item,
        spider
    ):
        return deferToThread(self._process_item_in_thread, item, spider)
    
    def _process_item_in_thread(self, item, spider):
        key = self.key % {'spider': spider.name}
        self.client.rpush(key, item['text'])
        return item

    def close_spider(self, spider):
        self.client.close()
