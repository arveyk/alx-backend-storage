#!/usr/bin/env python3
"""Redis module
"""
from collections.abc import Callable
import redis
from typing import Any
import uuid


class Cache:
    """Redis Cache Class
    """
    def __init__(self):
        """initializes the instances of Cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """
        Function to store Redis instance, generate random key using uuid
        and store input_data in redis using the random key
        Args:
            Data: data passed to the function
        Returns: a key string
        """
        self._redis = redis.Redis()
        key = str(uuid.uuid4())

        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable) -> Any:
        """
        Converts data to desired format using another callable function
        Args:
            key: data to convert
            fn: the function to call
        Returns: null if key is Null, the converted string otherwise
        """ 
        if key is None:
            return None
        if fn:
            fn(key)

    def get_str(self, data):
        """string from key
        """
        decoded = self._redis.get(data)
        return str(decode)

    def get_int(self, data):
        """
        Get int from string
        """
        decode = self._redis.get(data)
        return int(decode)


