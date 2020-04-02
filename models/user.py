#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from model_state import Base, State
from sqlalchemy import Column, Integer, String


class User(BaseModel):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'
    email = Column(String(128)Integer, nullable=False)
    password = Column(String(128)Integer, nullable=False)
    first_name = Column(String(128)Integer, nullable=True)
    last_name = Column(String(128)Integer, nullable=False)
