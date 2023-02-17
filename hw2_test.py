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

    def test_short_than1(self):
        duration1 = data.Duration(4, 30)
        duration2 = data.Duration(3, 20)
        time = hw2.shorter_duration_than(duration1, duration2)
        self.assertEqual(time, False)

    def test_short_than2(self):
        duration1 = data.Duration(4, 40)
        duration2 = data.Duration(5, 30)
        time = hw2.shorter_duration_than(duration1, duration2)
        self.assertEqual(time, True)

    def test_song_shorter_than1(self):
        list = [data.Song('Jimmy', 'School', data.Duration(4, 20))]









if __name__ == "main":
    unittest.main()
