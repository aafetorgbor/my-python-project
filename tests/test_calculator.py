"""
Unit tests for the Calculator module.
"""

import unittest
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition operation."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtract(self):
        """Test subtraction operation."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
    
    def test_multiply(self):
        """Test multiplication operation."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(-5, -3), 15)
        self.assertEqual(self.calc.multiply(0, 100), 0)
    
    def test_divide(self):
        """Test division operation."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertAlmostEqual(self.calc.divide(7, 3), 2.333333, places=5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))
    
    def test_power(self):
        """Test power operation."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(10, 0), 1)
        self.assertEqual(self.calc.power(2, -1), 0.5)
    
    def test_modulo(self):
        """Test modulo operation."""
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(15, 4), 3)
        self.assertEqual(self.calc.modulo(10, 5), 0)
        self.assertEqual(self.calc.modulo(7, 2), 1)
    
    def test_modulo_by_zero(self):
        """Test modulo by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.modulo(10, 0)
        self.assertIn("Cannot perform modulo with zero", str(context.exception))


if __name__ == '__main__':
    unittest.main()

# Made with Bob
