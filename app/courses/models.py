from flask_sqlalchemy import SQLAlchemy
from app import db

class Course(db.Model):
    __tablename__= 'course'
    id = db.Column(db.String(6), primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __repr__(self):
        return '<Id : %r , Name : %r>' %(self.id,self.name)
