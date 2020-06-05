import pymain
import unittest

class MyTests(unittest.TestCase):
    def test_doubleme(self):
        self.assertEqual(pymain.doubleme(2), 4)

# To Run: python3 -m unittest tests1
# Scan a tests directory in src for all files called test*.py: python3 -m unittest discover -s tests -t src