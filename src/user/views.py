from flask import Blueprint, jsonify, request
from .core import create_user, login as login_fn
from .errors import InvalidUserDataError


user = Blueprint('user', __name__)

@user.route("/login", methods=['POST'])
def login():
    try:
        user = login_fn(request.get_json())
        return jsonify(user)
    except InvalidUserDataError:
        return 'Invalid user data', 400

@user.route("/register", methods=['POST'])
def register():
    try:
        user = create_user(request.get_json())
        return jsonify(user)
    except InvalidUserDataError:
        return 'Invalid user data', 400

