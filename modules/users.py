from flask import request, Blueprint
import json
from bson import json_util, ObjectId
import database as db

devices_bp = Blueprint('users', __name__)

USER_DB = "users"

@devices_bp.route('/users', methods = ['GET'])
def getUsers():
    res = []
    for item in db.getAll(USER_DB):
        res.append(json.loads(json_util.dumps(item)))
    return {"data":res},200


@devices_bp.route('/user/<user_id>', methods = ['GET'])
def getUser(user_id):
    res = []
    for item in db.get(USER_DB, ObjectId(user_id)):
        res.append(json.loads(json_util.dumps(item)))
    return {"data":res},200


@devices_bp.route('/user', methods = ['POST'])
def addUser():
    req_data = request.get_json(force=True)
    return db.insert(USER_DB, req_data)


@devices_bp.route('/user/<user_id>', methods = ['PUT'])
def updateUser(user_id):
    req_data = request.get_json(force=True)
    return db.update(USER_DB, ObjectId(user_id), req_data)
