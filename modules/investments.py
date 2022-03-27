"""
Investment Portfolio

"""

from flask import request, Blueprint
import json
from bson import json_util, ObjectId
import database as db

devices_bp = Blueprint('investments', __name__, url_prefix='/investments')

DB_NAME = "investments"

# @devices_bp.route('/users', methods = ['GET'])
# def getUsers():
#     res = []
#     for item in db.getAll(DB_NAME):
#         res.append(json.loads(json_util.dumps(item)))
#     return {"data":res},200


@devices_bp.route('/<user_id>', methods = ['GET'])
def get_user_investments(user_id):
    req_data = request.get_json(force=True)
    req_data.update({"user_id":user_id})
    res = []
    for item in db.get(DB_NAME, req_data):
        res.append(json.loads(json_util.dumps(item)))
    return {"data":res},200


@devices_bp.route('/', methods = ['POST'])
def add_investments():
    req_data = request.get_json(force=True)
    return db.insert(DB_NAME, req_data)


@devices_bp.route('/<user_id>', methods = ['PUT'])
def update_investments(user_id):
    req_data = request.get_json(force=True)
    return db.update(DB_NAME, ObjectId(user_id), req_data)


# Data Models:

# user_record = {
#       "username":"ramsankar",
#       "password":"test123",
#       "email":"ramsankar123@gmail.com",
#       "mobile":"9874521110"
#     }
