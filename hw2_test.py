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
        list = [data.Song('Jimmy', 'School', data.Duration(4, 20)), data.Song('Timmy', 'Dance', data.Duration(3, 15)),
                data.Song("John", "Happy", data.Duration(5, 50)), data.Song("Paul", 'Sing', data.Duration(2, 13)),
                data.Song("Phil", 'Hit', data.Duration(3, 45)), data.Song('Sam', 'Jump', data.Duration(4, 35))]
        songs = hw2.song_shorter_than(list, data.Duration(4, 20))
        self.assertEqual(songs, [data.Song('Timmy', 'Dance', data.Duration(3, 15)),
                                 data.Song("Paul", 'Sing', data.Duration(2, 13)),
                                 data.Song("Phil", 'Hit', data.Duration(3, 45))])

    def test_song_shorter_than2(self):
        list = [data.Song('Jimmy', 'School', data.Duration(4, 20)), data.Song('Timmy', 'Dance', data.Duration(3, 15)),
                data.Song("John", "Happy", data.Duration(5, 50)), data.Song("Paul", 'Sing', data.Duration(2, 13)),
                data.Song("Phil", 'Hit', data.Duration(3, 45)), data.Song('Sam', 'Jump', data.Duration(4, 35))]
        songs = hw2.song_shorter_than(list, data.Duration(3, 20))
        self.assertEqual(songs, [data.Song('Timmy', 'Dance', data.Duration(3, 15)),
                                 data.Song("Paul", 'Sing', data.Duration(2, 13))])

    def test_running_time1(self):
        list = [data.Song('Jimmy', 'School', data.Duration(4, 20)), data.Song('Timmy', 'Dance', data.Duration(3, 15)),
                data.Song("John", "Happy", data.Duration(5, 50)), data.Song("Paul", 'Sing', data.Duration(2, 13)),
                data.Song("Phil", 'Hit', data.Duration(3, 45)), data.Song('Sam', 'Jump', data.Duration(4, 35))]
        play_list = [0, 5, 4, 8, 3, 3]
        running_time = hw2.running_time(list, play_list)
        self.assertEqual(running_time, data.Duration(17, 6))

    def test_running_time2(self):
        list = [data.Song('Jimmy', 'School', data.Duration(4, 20)), data.Song('Timmy', 'Dance', data.Duration(3, 15)),
                data.Song("John", "Happy", data.Duration(5, 50)), data.Song("Paul", 'Sing', data.Duration(2, 13)),
                data.Song("Phil", 'Hit', data.Duration(3, 45)), data.Song('Sam', 'Jump', data.Duration(4, 35))]
        play_list = [4, 2, 1, 5, 9, 3]
        running_time = hw2.running_time(list, play_list)
        self.assertEqual(running_time, data.Duration(19, 38))


    def test_validate_route1(self):
        link = [['san luis obispo', 'santa margarita'],
                ['san luis obispo', 'pismo beach'],
                ['atascadero', 'santa margarita'],
                ['atascadero', 'creston']]
        route = ['san luis obispo', 'atascadero']
        check = hw2.validate_route(link, route)
        self.assertEqual(check, False)









if __name__ == "main":
    unittest.main()
