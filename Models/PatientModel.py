from marshmallow import fields, Schema
import datetime
from .base import db


class PatientModel(db.Model):
    """
    User Model
    """

    # table name

    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, data):
        self.username = data['username']
        self.email = data['email']

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_users():
        return PatientModel.query.all()

    @staticmethod
    def get_one_user(id):
        return PatientModel.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)


class PatientSchema(Schema):
    """
  User Schema
  """
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
