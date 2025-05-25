from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import User, db

auth = Blueprint('auth', __name__)

@auth.route("/register", methods=["POST"])
def register():
    data = request.json
    user = User(email=data["email"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User created", "api_key": user.api_key})

@auth.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if user and user.check_password(data["password"]):
        token = create_access_token(identity=user.email)
        return jsonify(access_token=token, api_key=user.api_key)
    return jsonify({"msg": "Bad credentials"}), 401