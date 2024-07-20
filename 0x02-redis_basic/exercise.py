#!/usr/bin/env python3
"""
function that writes strings to redis
"""
import redis
import uuid
from typing import Union

class Cache:
    """ stores an instance of redis client """
    def __init__(self):
        self._redis = redis.Redis()

        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ generates random key """
        key = str(uuid.uuid4())

        self._redis.set(key, data)
        return key
