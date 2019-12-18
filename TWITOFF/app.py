"""code for app"""

from flask import Flask
from .models import DB
# app factory

def create_app():
    app = Flask(__name__)

# add config for db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
# have the db know about the app
    DB.init_app(app)


    @app.route('/')
    def root():
        return 'Welcome to Twitoff!'
    return app
