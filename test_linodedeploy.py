# test_linodedeploy.py
"""
Tests for LinodeDeploy module.
"""

import unittest
from linodedeploy import LinodeDeploy

class TestLinodeDeploy(unittest.TestCase):
    """Test cases for LinodeDeploy class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LinodeDeploy()
        self.assertIsInstance(instance, LinodeDeploy)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LinodeDeploy()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
