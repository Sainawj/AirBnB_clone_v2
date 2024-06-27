#!/usr/bin/python3
""" 
Tests for the State model.
"""
import os

from tests.test_models.test_base_model import TestBasemodel
from models.state import State


class TestState(TestBasemodel):
    """Tests for the State model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test case."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """Checks the name attribute type."""
        new = self.value()
        self.assertEqual(
            type(new.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

