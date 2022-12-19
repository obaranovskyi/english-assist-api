from flask import Flask
from src.database.db import db
from src.user.views import user
from src.word.views import word
from src.user.core import create_admin


app = Flask(__name__)

# configs
app.config.from_pyfile('src/config.py')

# views
app.register_blueprint(user, url_prefix='/users')
app.register_blueprint(word, url_prefix='/words')

# db
import src.user.entities
db.init_app(app)

# db creation
with app.app_context():
    # db.drop_all()
    db.create_all()
    create_admin()

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)
