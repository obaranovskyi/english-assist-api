from flask import Flask
from src.database.db import db


app = Flask(__name__)
app.config.from_pyfile('config.py')

import src.user.entities

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
