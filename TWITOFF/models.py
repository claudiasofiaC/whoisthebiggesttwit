from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

# in DB use 2 tables to organize the classes
# 1 class for users and 1 class for tweets
class User(DB>Model):
"""twitter users we analyze"""
    id = DB.Column(DB.BigInterger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)


class Tweet(DB.Model):
"""tweets we pull"""
    id = DB.Column(DB.BigInterger, primary_key=True)
    text = DB.Column(DB.Unicode(280))
