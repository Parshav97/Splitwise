from flask import Flask
from model.sqlalchemy import db
from model.UsersModel import UsersModel
from blueprints.user_blueprint import user_blueprint
from blueprints.expense_blueprint import expense_blueprint
# from config import Config

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)


app.register_blueprint(user_blueprint)
app.register_blueprint(expense_blueprint)


@app.route("/")
def index():
    return "<h1> Hello <h1>"

with app.app_context():
    db.create_all()

app.run(debug=True)