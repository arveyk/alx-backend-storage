#!/usr/bin/env python3
""" List all documents
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """Function to list all documents in a collection
    Args:
        mongo_collection: the collection to list
    Returns: empty lidy if no docs  are in the collection, list of
    documents otherwise
    """
    client = MongoClient()
    db = client.mongo_collection
    return db.find()
