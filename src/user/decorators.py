import jwt
from flask import request, jsonify
from functools import wraps
from .entities import User
from ..config import SECRET_KEY


def auth(fn):
    @wraps(fn)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers.get('Authorization').replace('Bearer ', '')
        if not token:
            return jsonify({ 'message': 'Token is missing.' }), 401
        try:
            data = jwt.decode(token, SECRET_KEY, "HS256")
            current_user = User.query.filter_by(public_id=data.get('public_id')).first()
        except Exception:
            return jsonify({ 'message': 'Token is invalid.' })
        return fn(current_user, *args, **kwargs)
    return decorated
