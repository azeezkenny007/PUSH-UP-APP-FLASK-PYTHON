from sqlalchemy import Column, Integer, String,create_engine,DateTime,Text,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from flask_login import UserMixin
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base,UserMixin):
    __tablename__ = 'users'
    id = Column("id",Integer, primary_key=True)
    name = Column("username",String(50))
    email = Column("email",String(120), unique=True)
    password=Column("password",String(120))
    workout =relationship("Workout",backref='author',lazy=True)

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User {self.name!r}>'
    
class Workout(Base):
    __tablename__="workouts"
    id = Column("id",Integer, primary_key=True)
    pushups =Column("pushup",Integer,nullable=False)
    date_posted =Column("date_posted",DateTime,nullable=False,default=datetime.utcnow)
    comment =Column("comment",Text,nullable=False)
    user_id=Column("user_id",Integer,ForeignKey("users.id"),nullable=False)
    
    
    

    
engine = create_engine('sqlite:///user.db',echo=True)
Base.metadata.create_all(bind=engine)
Session =sessionmaker(bind=engine)

session =Session()
session.close()