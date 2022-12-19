def to_user_dto(user, token):
    return {
        'id': user.public_id,
        'username': user.username,
        'admin': user.admin,
        'token': token
    }
