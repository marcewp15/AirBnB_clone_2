#!/usr/bin/python3
"""This is the review class"""
from models.base_model import Base, BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class Review(BaseModel, Base):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    __tablename__ = 'reviews'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=True)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=True)
    else:
        text = ""
        place_id = ""
        user_id = ""
