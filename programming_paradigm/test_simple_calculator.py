import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-4, 5), 1)
        self.assertEqual(self.calc.add(3,-9), -6)
        self.assertEqual(self.calc.add(8, 6), 14)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(7, 5), 2)
        self.assertEqual(self.calc.subtract(3, 4), -1)
        self.assertEqual(self.calc.subtract(8, 2), 6)
        self.assertEqual(self.calc.subtract(1, 4), -3)
        self.assertEqual(self.calc.subtract(4, 6), -2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(7, 5), 2)
        self.assertEqual(self.calc.multiply(3, 4), -1)
        self.assertEqual(self.calc.multiply(8, 2), 6)
        self.assertEqual(self.calc.multiply(1, 4), -3)
        self.assertEqual(self.calc.multiply(4, 6), -2)

    def test_division(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(6, 0), None)
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(5, 1), 5)
        self.assertEqual(self.calc.divide(10, 3), 3.3333)
        



# Remember to write additional test methods for subtract, multiply, and divide