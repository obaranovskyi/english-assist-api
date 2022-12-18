from flask import Flask
from src.database.db import db
from src.user.views import user


app = Flask(__name__)

# configs
app.config.from_pyfile('config.py')

# views
app.register_blueprint(user, url_prefix='/users')

# db
import src.user.entities
db.init_app(app)

# db creation
# with app.app_context():
#     db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
