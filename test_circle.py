import unittest
import math
from circle import area, perimeter



class CircleTestCase(unittest.TestCase) :
    def test_area_zero(self):
        self.assertAlmostEqual(area(0), 0)

    def test_area_one(self):
        self.assertAlmostEqual(area(1), math.pi)

    def test_area_two(self):
        self.assertAlmostEqual(area(2), 4 * math.pi)

    def test_area_three(self):
        self.assertAlmostEqual(area(3), 9 * math.pi)

    def test_perimeter_zero(self):
        self.assertAlmostEqual(perimeter(0), 0)

    def test_perimeter_one(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)

    def test_perimeter_two(self):
        self.assertAlmostEqual(perimeter(2), 2 * math.pi * 2)

    def test_perimeter_three(self):
        self.assertAlmostEqual(perimeter(3), 2 * math.pi * 3)