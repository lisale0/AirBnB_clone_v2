#!/usr/bin/python3
"""
Amenity Class from Models Module
"""
import os
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

class Amenity(BaseModel):
    """Amenity class handles all application amenities"""
    if (os.getenv('HBNB_TYPE_STORAGE') == 'db'):
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new amenity"""
        super().__init__(self, *args, **kwargs)
