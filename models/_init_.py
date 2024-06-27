#!/usr/bin/python3
"""Instantiates a FileStorage or DBStorage object based on environment.

Creates a single instance of FileStorage or DBStorage depending on the value
of HBNB_TYPE_STORAGE environment variable.
"""
import os

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

# Instantiate a storage object based on environment variable
storage = DBStorage() if os.getenv('HBNB_TYPE_STORAGE') == 'db' else FileStorage()

# Reload the storage instance
storage.reload()

