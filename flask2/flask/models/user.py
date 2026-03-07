from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
from .base import Base


class User(Base):
    __tablename__ = "users"

    id =  Column(Integer, primary_key=True, index = True)
    login = Column(String(50), unique = True, nullable = False)
    password = Column(String(128), nullable = False)
    gender = Column(String(10), nullable = False)
    name = Column(String(25), nullable = False)

    def __init__(self, login, password, gender, name):
        self.login = login
        self.password = password
        self.gender = gender
        self.name = name