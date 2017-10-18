""" Test cases """
import unittest
from prodsum import Prodsum


class BasicTest(unittest.TestCase):
    """ Basic tests """
    def test_add(self):
        """ Addition test"""
        calc = Prodsum()
        result = calc.add(2, 3)
        self.assertEqual(5, result)

    def test_product(self):
        """ Product test"""
        calc = Prodsum()
        result = calc.multiply(2, 3)
        self.assertEqual(6, result)

if __name__ == '__main__':
    unittest.main()
