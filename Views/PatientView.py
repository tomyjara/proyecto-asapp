from flask import request, json, Response, Blueprint
from Models.PatientModel import PatientModel, PatientSchema

user_api = Blueprint('users', __name__)
user_schema = PatientSchema()

@user_api.route('/create', methods=['POST'])
def create():
    """
    Create User Function
    """
    req_data = request.get_json()
    data, error = user_schema.load(req_data)
    body = request.json
    if error:
        return custom_response(error, 400)

    # check if user already exist in the db
    # user_in_db = PatientModel.get_user_by_email(data.get('email'))
    # if user_in_db:
    #    message = {'error': 'User already exist, please supply another email address'}
    #    return custom_response(message, 400)

    user = PatientModel(data)
    user.save()

    user_data = user_schema.dump(user).data

    return custom_response(user_data, 200)


@user_api.route('/', methods=['GET'])
def get_all():
    users = PatientModel.get_all_users()
    ser_users = user_schema.dump(users, many=True).data
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
