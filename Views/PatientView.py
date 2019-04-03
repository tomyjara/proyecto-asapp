from flask import request, json, Response, Blueprint
from Models.PatientModel import PatientModel, PatientSchema

patient_api = Blueprint('patients', __name__)
patient_schema = PatientSchema()


@patient_api.route('', methods=['POST'])
def create():
    """
    Create Patient Function
    """
    req_data = request.get_json()
    data, error = patient_schema.load(req_data)
    if error:
        return custom_response(error, 400)

    #user_in_db = PatientModel.get_user_by_email(data.get('email'))
    #if user_in_db:
    #    message = {'error': 'User already exist, please supply another email address'}
    #    return custom_response(message, 400)

    patient = PatientModel(data)
    patient.save()

    patient_data = patient_schema.dump(patient).data

    return custom_response(patient_data, 200)


@patient_api.route('', methods=['GET'])
def get_all():
    patients = PatientModel.get_all_patients()
    ser_users = patient_schema.dump(patients, many=True).data
    return custom_response(ser_users, 200)


@patient_api.route('/<id>', methods=['GET'])
def get(id):
    patient = PatientModel.get_one_patient(id)
    ser_users = patient_schema.dump(patient).data
    return custom_response(ser_users, 200)


@patient_api.route('/<id>', methods=['DELETE'])
def delete(id):
    user = PatientModel.get_one_patient(id)
    ser_users = patient_schema.dump(user).data
    user.delete()
    return custom_response(ser_users, 200)


@patient_api.route('/<id>', methods=['PUT'])
def put(id):
    req_data = request.get_json()
    data, error = patient_schema.load(req_data)

    user = PatientModel.get_one_patient(id)
    user.update(data)

    ser_users = patient_schema.dump(user).data

    return custom_response(ser_users, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
