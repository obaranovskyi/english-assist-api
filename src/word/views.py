from flask import Blueprint


word = Blueprint('word', __name__)

@word.route("/")
def words():
  return 'Word list'

