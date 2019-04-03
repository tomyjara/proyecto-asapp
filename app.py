from flask import Flask
from sqlalchemy_utils import create_database, database_exists
from flask_migrate import Migrate

import os




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

    from Views.PatientView import patient_api as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/api/patients')

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
