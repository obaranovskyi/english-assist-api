from flask import Blueprint


user = Blueprint('user', __name__, template_folder='templates')

@user.route("/login")
def login():
  return 'Login user'

@user.route("/register")
def register():
  return 'Register user'
