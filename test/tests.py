#!/usr/bin/env python3
import unittest

# The function to be tested
def add_numbers(a, b):
    return a + b

# Test class inheriting from unittest.TestCase
class TestAddNumbers(unittest.TestCase):

    # Test method
    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)  # Assertion to check if the result is as expected

        result = add_numbers(-1, 5)
        self.assertEqual(result, 4)  # Another assertion

        result = add_numbers(0, 0)
        self.assertEqual(result, 0)  # And another assertion

# Run the tests
if __name__ == '__main__':
    unittest.main()

