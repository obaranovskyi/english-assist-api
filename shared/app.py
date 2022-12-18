from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'tempsecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///english_assist.db'
