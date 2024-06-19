#!/usr/bin/env python3
"""Redis module
"""
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
