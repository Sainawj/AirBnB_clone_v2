#!/usr/bin/python3
"""
State module for AirBnB clone.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """State class for handling states in the AirBnB clone."""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        """Return a list of City objects related to the State."""
        from models import storage
        all_cities = storage.all(City)
        state_cities = [city for city in all_cities.values() if city.state_id == self.id]
        return state_cities
