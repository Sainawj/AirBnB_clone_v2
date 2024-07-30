#!/usr/bin/python3
"""
DBStorage engine for AirBnB clone.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """DBStorage class for handling storage of objects in a database."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage engine."""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')
            ),
            pool_pre_ping=True
        )
        Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """Return a dictionary of all objects or objects of a specific class."""
        if cls is None:
            result = {}
            for class_name in [State, User, City, Place, Review, Amenity]:
                objects = self.__session.query(class_name).all()
                for obj in objects:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    result[key] = obj
            return result
        else:
            result = {}
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = f"{obj.__class__.__name__}.{obj.id}"
                result[key] = obj
            return result

    def new(self, obj):
        """Add a new object to the session."""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit the current session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the session."""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """Reload the session with the database engine."""
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Remove the current session."""
        self.__session.remove()
