import pymongo
import os

client = pymongo.MongoClient(os.getenv('db_client'))
famfin_db = client["finfam"]

def getAll(collection):
    return famfin_db[collection].find()


def get(collection, record):
    return famfin_db[collection].find(record)


def insert(collection, record):
    try:
        result = famfin_db[collection].insert_one(record)
    except pymongo.errors.DuplicateKeyError:
        return {"result":"Duplicate - Failure"}
    return {"result":"Success"}


def update(collection, record_id, upd_doc):
    famfin_db[collection].find_one_and_update({"_id": record_id},
                                 {"$set": upd_doc})
    return {"result":"Success"}