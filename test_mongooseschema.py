# test_mongooseschema.py
"""
Tests for MongooseSchema module.
"""

import unittest
from mongooseschema import MongooseSchema

class TestMongooseSchema(unittest.TestCase):
    """Test cases for MongooseSchema class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MongooseSchema()
        self.assertIsInstance(instance, MongooseSchema)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MongooseSchema()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
