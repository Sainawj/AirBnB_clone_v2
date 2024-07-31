#!/usr/bin/python3
"""Holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    def __init__(self, *args, **kwargs):
        """Initializes state"""
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """Getter for list of city instances related to the state"""
        from models import storage  # Delayed import
        city_list = []
        all_cities = storage.all(City)
        for city in all_cities.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
