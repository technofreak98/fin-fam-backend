"""
Investment Portfolio

"""

from flask import request, Blueprint
import json
from bson import json_util, ObjectId
import database as db
import numpy as np

devices_bp = Blueprint('investments', __name__, url_prefix='/investments')

DB_NAME = "investments"


@devices_bp.route('/<user_id>', methods = ['GET'])
def get_user_investments(user_id):
    req_data = {"user_id":user_id}
    investment_data = json.loads(json_util.dumps(db.get(DB_NAME, req_data)))[0]
    worth = list({key: value} for key, value in investment_data.items() if not key in ['_id','user_id'])
    res = {'investment_id':investment_data['_id'],'worth':worth}
    return {"data": [res]},200


@devices_bp.route('/', methods = ['POST'])
def add_investments():
    req_data = request.get_json(force=True)
    return db.insert(DB_NAME, req_data)


@devices_bp.route('/<user_id>', methods = ['PUT'])
def update_investments(user_id):
    req_data = request.get_json(force=True)
    return db.update(DB_NAME, ObjectId(user_id), req_data)


@devices_bp.route('/total/<user_id>', methods = ['GET'])
def get_total_user_investments(user_id):
    req_data = {"user_id":user_id}
    investment_data = json.loads(json_util.dumps(db.get(DB_NAME, req_data)))[0]
    res = np.sum(float(value) for key, value in investment_data.items() if not key in ['_id','user_id'])
    return {"data":res},200
