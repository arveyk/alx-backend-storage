#!/usr/bin/env python3
"""Redis module
"""
import redis
import uuid


class Cache():
    """Redis Cache Class
    """
    def __init__(self):
        """initializes the instances of Cache class
        """
        _redis = redis.Redis()
        _redis.flushdb()

    def store(self, data: any) -> str:
        """
        """
        red = redis.Redis()
        # generate random key using uuid
        key = str(uuid.uuid4())
        
        # store input_data in redis using the random key
        red.set(key, data)
        return key
