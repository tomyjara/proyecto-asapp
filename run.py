import os

from flask_sqlalchemy import SQLAlchemy

from app import create_app

if __name__ == '__main__':

  app = create_app()
  #db = SQLAlchemy(app)
  # run app
  app.run()