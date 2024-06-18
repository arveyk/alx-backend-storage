#!/usr/bin/env python3
"""Listing documents base on condition
"""

def schools_by_topic(mongo_collection, topic):
    """ Function to list school having a specific topic
    Args:
        mongo_collection: the pymongo collection object
        topic: the topic used to filter search
    Returns: the list of schools
    """
    school = mongo_collection.find({"topics": topic})
    return school
