from flask_sqlalchemy import SQLAlchemy
from app import db

class Enroll(db.Model):
    __tablename__= 'enroll'
    key = db.Column(db.Integer, primary_key=True,autoincrement=True)
    roll = db.Column(db.String(8))
    id = db.Column(db.String(6))

    def __init__(self,roll,id):
        self.roll = roll
        self.id = id
    def __repr__(self):
        return '<Id : %r , Roll : %r>' %(self.id,self.roll)
