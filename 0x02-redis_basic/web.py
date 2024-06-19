#!/usr/bin/env python3
""" Expiring web cache and tracker
"""
import redis
import requests

def get_page(url: str) -> str:
    """
    Function that obtains contents from the url and returns it
    """
    red = redis.Redis()
    count = 0
    res = ["string"]
    with requests.Session() as s:
        res[0] = s.get(url)
        count += 1
    red.setex(count, 10, url)
    return res[0]
