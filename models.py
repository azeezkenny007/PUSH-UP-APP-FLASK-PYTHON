
from sqlalchemy import Column, Integer, String,create_engine
from sqlalchemy.orm import sessionmaker,relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column("id",Integer, primary_key=True)
    name = Column("username",String(50))
    email = Column("email",String(120), unique=True)
    password=Column("password",String(120))

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User {self.name!r}>'
    
engine = engine = create_engine('sqlite:///user.db',echo=True)
Base.metadata.create_all(bind=engine)
Session =sessionmaker(bind=engine)

session =Session()
session.close()