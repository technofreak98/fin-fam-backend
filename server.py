from flask import Flask, request
import json
from bson import json_util, ObjectId
import database

app = Flask(__name__)

@app.route('/users', methods = ['GET'])
def getUsers():
    res = []
    for item in database.getAll("user_collection"):
        res.append(json.loads(json_util.dumps(item)))
    return {"data":res},200

@app.route('/user/<user_id>', methods = ['GET'])
def getUser(user_id):
    print(user_id)
    res = []
    for item in database.get("user_collection", ObjectId(user_id)):
        res.append(json.loads(json_util.dumps(item)))
    return {"data":res},200

@app.route('/user', methods = ['POST'])
def addUser():
    req_data = request.get_json(force=True)
    user_record = req_data
    return database.insert("user_collection", user_record)

@app.route('/user/<user_id>', methods = ['PUT'])
def updateUser(user_id):
    req_data = request.get_json(force=True)
    return database.update("user_collection", ObjectId(user_id), req_data)


if __name__ == "__main__":
  app.run()

# Data Models:

# user_record = {
#       "username":"ramsankar",
#       "password":"test123",
#       "email":"ramsankar123@gmail.com",
#       "mobile":"9874521110"
#     }
