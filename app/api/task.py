from app import mongo
from app.func import serialize_doc
from flask import ( Flask , 
    Blueprint, flash, jsonify, abort, request
)

import uuid

bp = Blueprint('task', __name__, url_prefix='/')


@bp.route('/register', methods=["POST"])
def register():   
    if not request.json:
        abort(500)

    username = request.json.get("username", None)
    password = request.json.get("password", None)
    name = request.json.get("name", None)

    if username is None or password is None or name is  None:
         return jsonify(message="Invalid Request") , 500 
    
    id = uuid.uuid4().hex

    tasks = mongo.db.task.insert_one({
        "id"       : id,
        "username" : username,
        "password" : password,
        "name" : name
    }).inserted_id
    return jsonify({"status" : "created success fully"}) 




@bp.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 500

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 500
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 500

    users = mongo.db.task.find_one({"username" : username})
   

    if users is None:
        return (jsonify("username failed!")), 400
    
    users = mongo.db.task.find_one({"password" : password})
    
    if users is None:
        return (jsonify("password failed!")), 400


    return jsonify({"status" : "return successfully"})