#!/usr/bin/python3
"""
FileStorage engine for AirBnB clone.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """FileStorage class for handling storage of objects"""

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Return a dictionary of all objects or objects of a specific class."""
        if cls is None:
            return self.__objects
        else:
            filtered_objects = {}
            for key, obj in self.__objects.items():
                if isinstance(obj, cls):
                    filtered_objects[key] = obj
            return filtered_objects

    def new(self, obj):
        """Add a new object to the storage."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Save the objects to a JSON file."""
        with open(self.__file_path, 'w') as file:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, file)

    def reload(self):
        """Reload objects from the JSON file."""
        try:
            with open(self.__file_path, 'r') as file:
                objects = json.load(file)
                for key, value in objects.items():
                    cls_name = value['__class__']
                    cls = globals()[cls_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

    def close(self):
        """Call reload to deserialize the JSON file to objects."""
        self.reload()
