import data
import math

# Part 1
"""
For part one, my function create_rectangle takes in 2 inputs of data type Point, and returns 1 output of data type 
Rectangle. The purpose of this function is the use the two input points and create a Rectangle object. Since
we do not know the top_left and bottom_right attributes, this function finds those based on the given points 
to pass to the Rectangle object.
"""


def create_rectangle(point1: data.Point, point2: data.Point) -> data.Rectangle:
    if abs(point1.x) > abs(point2.x):
        if point1.x > 0:
            right = point1.x
            left = point2.x
        else:
            right = point2.x
            left = point1.x
    elif abs(point1.x) < abs(point2.x):
        if point2.x > 0:
            right = point2.x
            left = point1.x
        else:
            right = point1.x
            left = point2.x

    if abs(point1.y) > abs(point2.y):
        if point1.y > 0:
            top = point1.y
            bottom = point2.y
        else:
            top = point2.y
            bottom = point1.y
    elif abs(point1.y) < abs(point2.y):
        if point2.y > 0:
            top = point2.y
            bottom = point1.y
        else:
            top = point1.y
            bottom = point2.y
    top_left = (left, top)
    bottom_right = (right, bottom)

    return data.Rectangle(top_left, bottom_right)


#Part 2
"""
For part 2 my function shorter_duration_than takes in 2 inputs of data type Duration. This function returns one output 
of type boolean. The purpose of this function is to compare the two inputs return True if the first duration is 
smaller than the second duration, and false otherwise.
"""
def shorter_duration_than(dur1: data.Duration, dur2: data.Duration) -> bool:
    if dur1.minutes < dur2.minutes:
        return True
    elif dur1.minutes > dur2.minutes:
        return False
    elif dur1.minutes == dur2.minutes:
        if dur1.seconds < dur2.seconds:
            return True
        else:
            return False

#Part 3
"""
For part three my function song_shorter_than takes in two inputs, the first of type list[data.Song] and the second of 
data type Duration. The output of this function is lf list[data.Song]. The purpose of this function is to make a list
of elements with data type Song from another list of elements with data type Song if the duration of the song is below
a certain time.

"""
def song_shorter_than(songs: list[data.Song], dur: data.Duration) -> list[data.Song]:
    new_song = []
    for s in songs:
        if s.duration.minutes < dur.minutes:
            new_song.append(s)
        elif s.duration.minutes == dur.minutes:
            if s.duration.seconds < dur.seconds:
                new_song.append(s)
    return new_song

def running_time(songs: list[data.Song], play_list: list) -> data.Duration:
    time = data.Duration(0, 0)
    for k in play_list:
        if k < len(songs):
            time.minutes = time.minutes + songs[k].duration.minutes
            time.seconds = time.seconds + songs[k].duration.seconds
        if time.seconds > 60:
            time.seconds -= 60
            time.minutes += 1

    return time



def validate_route(city_links: list[list[str]], route: list[str]) -> bool:






