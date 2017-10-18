""" Test cases """
import unittest
from diffps import Diffps


class BasicTest(unittest.TestCase):
    """ Basic tests """
    def test_add(self):
        """ Addition test"""
        calc = Diffps()
        result = calc.add(2, 3)
        self.assertEqual(5, result)

    def test_product(self):
        """ Product test"""
        calc = Diffps()
        result = calc.multiply(2, 3)
        self.assertEqual(6, result)

if __name__ == '__main__':
    unittest.main()
