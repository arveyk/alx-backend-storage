#!/usr/bin/env python3
""" Sorted by average score
"""

def top_students(mongo_collection):
    """
    """
    students = mongo_collection.aggregate([{
        '$group': {
            'average_score': {'$avg': score}
            }}])
    return students
