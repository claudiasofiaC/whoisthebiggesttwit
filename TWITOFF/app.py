"""code for app"""
# alphabetical order is the norm

from decouple import config
from flask import Flask, render_template, request
from .models import DB, User
# app factory


def create_app():
    app = Flask(__name__)

# add config for db
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
# have the db know about the app
    DB.init_app(app)

# stop tracking mods on SQLAlchemy
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    @app.route('/')
    def root():
        #dont forget to import User from .models
        users = User.query.all()
        return render_template('base.html', title = 'Home', users=users)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title = 'Reset', users=[])

    return app
# had a bug with decouple install
# had to pip install python_decouple
