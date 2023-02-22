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


"""
Part 4
For this part, my function running_time takes in 2 parameters, the first of type list[data.Song] and the second of
type list. The function returns an output of data type Duration. The purpose of this function is to take the second 
list, which acts as a playlist, and see how much time all the songs in the 'playlist' are in total by comparing
to the first list.
"""

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
"""
Part 5
For this function validate_route, it takes 2 parameters. One of type list[list[str]] and the other of type list[str]. 
The output of this function is of the boolean type. The purpose of this function is to see if the route provided in 
the second list is valid by comparing with the first list[list[str]].
"""


def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
    if len(city_links) == 0:
        return False
    elif len(route) == 0:
        return True
    elif len(route) == 1:
        return True
    for idx in range(1,len(route),1):
        #if idx < len(route) - 1:
        valid = False
        for k in city_links:
            if route[idx-1] in k and route[idx] in k:
                valid = True
        if valid == False:
            return False
    return valid


def help(ints, start_range):
    max = 0
    current = 0
    if start_range > len(ints) - 1:
        return max
    for int in range (start_range, len(ints)):
        if int < len(ints) - 1:
            if ints[int] == ints[int+1]:
                current += 1
                if current > max:
                    max = current
            if ints[int] != ints[int+1]:
                return max
        else:
            return max


"""
Part 6
For this function longest_repitition, it takes in one parameter of type list[int]. The function returns None if the 
list is empty and returns the idx of the longest repition of numbers if the list is not empty. 
"""

def longest_repitition(ints: list[int]):
    list_max = 0
    max_idx = 0
    if len(ints) == 0:
        return None
    for k in range(len(ints)):
        if help(ints, k) > list_max:
            a = help(ints, k)
            list_max = a
            max_idx = k
    return max_idx

"""
First attempt 

    count = 1
    top = 0
    if len(num) == 0:
        return None
    for idx in range(len(num)):
        if idx < len(num) - 1:
            print("idx:" + str(idx))
            if num[idx] == num[idx + 1]:
                count += 1
                print(count)

            if num[idx] != num[idx + 1]:
                print("true")
                if count < top:
                    print("double true")
                    top = count
                    print("idx1" + str(idx) + "count" + str(top))
                    idx_store = idx - (count - 1)
                    print("store" + str(idx_store))
                    count = 1

                else:
                    count = 1

            if idx == len(num) - 2:
                if count < top:
                    print("double true")
                    top = count
                    print("idx1" + str(idx) + "count" + str(top))
                    idx_store = idx - (count - 1)
                return idx_store

"""















