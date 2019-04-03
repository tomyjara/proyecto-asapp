from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow, fields
from sqlalchemy_utils import create_database, database_exists
from flask_migrate import Migrate

import os
from Views.PatientView import user_api as user_blueprint

'''
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    conditions = db.relationship('Condition', backref='conditions', lazy=True)


    def __init__(self, username, email):
        self.username = username
        self.email = email


class Condition(db.Model):

    __tablename__ = 'conditions'
    id = db.Column(db.Integer, primary_key=True)
    alive = db.Column(db.Boolean, nullable=False)
    text = db.Column(db.String(120), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, text, alive, patient_id):
        self.alive = alive
        self.text = text
        self.patient_id = patient_id


class ConditionSchema(ma.Schema):
    class Meta:
        fields = ('patient_id', 'text', 'alive')


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'conditions')

user_schema = UserSchema(ma)
users_schema = UserSchema(many=True)

condition_schema = ConditionSchema(ma)
conditions_schema = ConditionSchema(many=True)

# endpoint to create new user

@app.route("/user", methods=["POST"])
def add_user():
    username = request.json['username']
    email = request.json['email']

    new_user = User(username, email)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

@app.route("/condition", methods=["POST"])
def add_condition():

    text = request.json['text']
    alive = request.json['alive']
    patient_id = request.josn['patient_id']

    new_condition = Condition(text, alive, patient_id)

    db.session.add(new_condition)
    db.session.commit()

    return condition_schema.jsonify(new_condition)


# endpoint to show all users
@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    response = jsonify(result.data)
    return response



# endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


# endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    username = request.json['username']
    email = request.json['email']

    user.email = email
    user.username = username

    db.session.commit()
    return user_schema.jsonify(user)


# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)

'''


def create_app():
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
    db_url = app.config["SQLALCHEMY_DATABASE_URI"]

    if not database_exists(db_url):
        create_database(db_url)

    # register sqlalchemy to this app

    from Models.base import db

    db.init_app(app)  # initialize Flask SQLALchemy with this flask app
    Migrate(app, db)

    from Views.PatientView import user_api as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/api/users')

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return 'Congratulations! Your first endpoint is working'

    return app


'''
if __name__ == '__main__':
    app.run(debug=True)
    '''
