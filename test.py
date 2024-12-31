# test_string_reverse.py
import unittest
from string_reverse import reverse_string

class TestStringMethods(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")
        self.assertEqual(reverse_string(""), "")  # Empty string test
        self.assertEqual(reverse_string("a"), "a")  # Single character test

if __name__ == "__main__":
    unittest.main()
