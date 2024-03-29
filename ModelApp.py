import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#Try it later
Migrate(app,db)
###########################
class teacher(db.Model):

    __tablename__ = 'teachers'

    id = db.Column(db.Integer,primary_key=True)
    fullname = db.Column(db.Text)
    email = db.Column(db.Text)

    def __init__(self,fullname,email):
        self.fullname = fullname
        self.email = email

    def __repr__(self):
        return f" thankyou  {self.fullname} sign up successful."
