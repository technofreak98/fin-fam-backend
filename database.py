import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
famfin_db = client["FamFin"]

def getAll(collection):
    return famfin_db[collection].find()

def get(collection, record_id):
    return famfin_db[collection].find({"_id": record_id})

def insert(collection, record):
    try:
        result = famfin_db[collection].insert_one(record)
    except pymongo.errors.DuplicateKeyError:
        return {"result":"Duplicate - Failure"}
    return {"result":"Success"}

def update(collection, record_id, upd_doc):
    print(collection, record_id)
    famfin_db[collection].find_one_and_update({"_id": record_id}, 
                                 {"$set": upd_doc})
    return {"result":"Success"}