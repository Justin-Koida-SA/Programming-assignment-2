import data
import unittest
import math
import hw2


class TestCases(unittest.TestCase):

    def test_create_rectangle1(self):
        point1 = data.Point(7, 12)
        point2 = data.Point(-4, 8)
        create = hw2.create_rectangle(point1, point2)
        self.assertEqual(create, data.Rectangle((-4, 12), (7, 8)))

    def test_create_rectangle2(self):
        point1 = data.Point(-14, -4)
        point2 = data.Point(-1, -8)
        create = hw2.create_rectangle(point1, point2)
        self.assertEqual(create, data.Rectangle((-14, -4), (-1, -8)))










if __name__ == "main":
    unittest.main()
