import unittest
from square import *


class squareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_int_area(self):
        res = area(5);
        self.assertEqual(res, 25)

    def test_float_area(self):
        res = area(5.25)
        self.assertAlmostEqual(res, 27.5, delta=0.1)
    
    def test_minus_area(self):
        with self.assertRaises(Exception):
            area(-3)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_int_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_float_perimeter(self):
        res = perimeter(5.9)
        self.assertEqual(res, 23.6)
        
    def test_minus_perimeter(self):
        with self.assertRaises(Exception):
            perimeter(-3)