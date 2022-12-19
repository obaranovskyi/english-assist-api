from flask import Blueprint

from ..user.decorators import auth


word = Blueprint('word', __name__)

@word.route("/", methods=['GET'])
@auth
def words(current_user):
    print(current_user)
    return 'Word list'

