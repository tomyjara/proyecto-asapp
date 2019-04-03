from marshmallow import fields, Schema
from .base import db


class PatientModel(db.Model):
    """
    Patient Model
    """

    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, data):
        self.patient_name = data['patient_name']
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
    def get_all_patients():
        return PatientModel.query.all()

    @staticmethod
    def get_one_patient(id):
        return PatientModel.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)


class PatientSchema(Schema):
    """
    Patient Schema
    """

    id = fields.Int(dump_only=True)
    patient_name = fields.Str(required=True)
    email = fields.Email(required=True)
