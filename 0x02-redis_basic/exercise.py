#!/usr/bin/env python3
"""Redis module
"""
import redis
from typing import Any
import uuid


class Cache:
    """Redis Cache Class
    """
    def __init__(self) -> None:
        """initializes the instances of Cache class
        """
        _redis = redis.Redis()
        _redis.flushdb()

    def store(self, data: Any) -> str:
        """
        Function to store Redis instance
        Args:
            Data: data passed to the function
        Returns: a key string
        """
        red = redis.Redis()
        """generate random key using uuid"""
        key = str(uuid.uuid4())

        # store input_data in redis using the random key
        red.set(key, data)
        return key
