import uuid
import jwt
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from .dto import to_user_dto
from .entities import User
from ..database.db import db
from ..config import SECRET_KEY


def create_user(user):
    username = user.get('username')
    password = user.get('password')
    if not username or not password:
        raise ValueError()
    hashed_password = generate_password_hash(password, method='sha256')
    user = User(
        public_id=str(uuid.uuid4()),
        username=username,
        password=hashed_password,
    )
    db.session.add(user)
    db.session.commit()
    return to_user_dto(user, generate_jwt_token(user))

def login(user):
    username = user.get('username')
    password = user.get('password')
    if not username or not password:
        raise ValueError()
    user = User.query.filter_by(username=username).first()
    if not user:
        raise ValueError()
    print(password, user.password, check_password_hash(password, user.password))
    if not check_password_hash(user.password, password):
        raise ValueError()
    return to_user_dto(user, generate_jwt_token(user))
        
def generate_jwt_token(user):
    return jwt.encode({
        'id': user.public_id,
        'exp': datetime.utcnow() + timedelta(days=3)
    }, SECRET_KEY, algorithm="HS256")
