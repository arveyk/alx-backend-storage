#!/usr/bin/env python3
"""Inserting into mongodb database
"""


def insert_school(mongo_collection, **kwargs):
    """ Function to insert a new document in a collection
    Args:
        mongo_collection: pymongo collection object
        kwargs: arguments determining what to add into the collection
    Returns: the new _id
    """

