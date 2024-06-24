import json
from typing import List

from config import settings
from redis import Redis, from_url


class RedisClient:
    def __init__(
        self,
    ) -> None:
        self.client = Redis(password=self.R_PASSWORD)

    def _convert_data_from_json(self, data):
        try:
            return json.loads(data)
        except Exception as err:
            print(f"Failed to convert data into dict, encountered error: {err}")
            raise err

    def _convert_data_to_json(self, data):
        try:
            return json.dumps(data)
        except Exception as err:
            print(f"Failed to convert data into json, encountered error: {err}")
            raise err

    def send_data_to_pipeline(self, data):
        data = self._convert_data_to_json(data)
        self.connection.lpush(self.key, data)

    def close(self) -> None:
        if self.client:
            self.client.close()
