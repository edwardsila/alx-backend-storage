#!/usr/bin/env python3
"""
mongoDB operations with
python using pymongo
"""

def list_all(mongo_collection):
    """ list all documents in the db """
    docs = mongo_collection.find()

    if docs.count() == 0:
        return []
    return docs
