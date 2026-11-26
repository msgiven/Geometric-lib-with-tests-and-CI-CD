import unittest
import math
from square import area, perimeter

class SquareTestCase(unittest.TestCase) :
    def test_area_zero(self):
        self.assertAlmostEqual(area(0), 0)

    def test_area_one(self):
        self.assertAlmostEqual(area(1), 1)

    def test_area_two(self):
        self.assertAlmostEqual(area(2), 4)

    def test_area_three(self):
        self.assertAlmostEqual(area(3), 9)

    def test_perimeter_zero(self):
        self.assertAlmostEqual(perimeter(0), 0)

    def test_perimeter_one(self):
        self.assertAlmostEqual(perimeter(1), 4)

    def test_perimeter_two(self):
        self.assertAlmostEqual(perimeter(2), 8)

    def test_perimeter_three(self):
        self.assertAlmostEqual(perimeter(3), 12)