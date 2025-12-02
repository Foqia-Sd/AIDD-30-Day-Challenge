import unittest
from unittest.mock import patch
import sys
from io import StringIO

from calculator.input_parser import get_numerical_input, get_operator_input

class TestInputParser(unittest.TestCase):

    @patch('builtins.input', side_effect=['5'])
    def test_get_numerical_input_valid(self, mock_input):
        self.assertEqual(get_numerical_input("Enter a number: "), 5.0)

    @patch('builtins.input', side_effect=['abc', '10'])
    def test_get_numerical_input_invalid_then_valid(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            self.assertEqual(get_numerical_input("Enter a number: "), 10.0)
            self.assertIn("Error: Invalid input. Please enter a number.", fake_stdout.getvalue())

    @patch('builtins.input', side_effect=['+'])
    def test_get_operator_input_valid(self, mock_input):
        self.assertEqual(get_operator_input("Enter an operator: "), '+')

    @patch('builtins.input', side_effect=['&', '*'])
    def test_get_operator_input_invalid_then_valid(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            self.assertEqual(get_operator_input("Enter an operator: "), '*')
            self.assertIn("Error: Invalid operator. Please use +, -, *, or /.", fake_stdout.getvalue())

from calculator.operations import add, subtract, multiply, divide, perform_calculation

class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(2.5, 3.5), 6.0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(2, 5), -3)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(5.5, 2.5), 3.0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(-2, -4), 8)
        self.assertEqual(multiply(2.5, 2), 5.0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2.0)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(-10, -5), 2.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_perform_calculation(self):
        self.assertEqual(perform_calculation(5, 2, '+'), 7)
        self.assertEqual(perform_calculation(5, 2, '-'), 3)
        self.assertEqual(perform_calculation(5, 2, '*'), 10)
        self.assertEqual(perform_calculation(10, 2, '/'), 5.0)
        self.assertEqual(perform_calculation(10, 0, '/'), "Error: Division by zero is not allowed.")
        self.assertEqual(perform_calculation(5, 2, '&'), "Error: Invalid operator.")

if __name__ == '__main__':
    unittest.main()

