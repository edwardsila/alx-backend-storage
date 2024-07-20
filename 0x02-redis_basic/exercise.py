#!/usr/bin/env python3
"""
function that writes strings to redis
"""
import redis
import uuid
from typing import Union, Callable, Optional, Any


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

    def get(
      self,
      key: str,
      fn: Optional[Callable[[bytes], Any]] = None
    ) -> Any:
        value = self._redis.get(key)

        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, fn=int)
