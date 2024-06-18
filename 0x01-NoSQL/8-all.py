#!/usr/bin/env python3
""" List all documents
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """Function to list all documents in a collection
    Args:
        mongo_collection: the collection to list
    Returns: empty lidy if no docs  are in the collection, list of
    documents otherwise """
    docs = {}
    collection = mongo_collection.find()
    for key, value in collection:
        if key == "_id":
            docs.key = collection.key
    return docs
