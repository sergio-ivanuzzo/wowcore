import asyncio_redis
import json

from Typings.Abstract.AbstractBase import AbstractBase


class RedisConnection(AbstractBase):

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.connection = None

    async def set(self, key: str, value):
        connection = await asyncio_redis.Connection.create(host=self.host, port=self.port)
        await connection.set(key, json.dumps(value))
        connection.close()

    async def get(self, key):
        connection = await asyncio_redis.Connection.create(host=self.host, port=self.port)
        result = await connection.get(key)
        connection.close()
        return json.loads(result)

    @staticmethod
    def create():
        return RedisConnection(
            host=RedisConnection.from_config('server:connection:redis_server:host'),
            port=RedisConnection.from_config('server:connection:redis_server:port'),
        )
