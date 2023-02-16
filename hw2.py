import data
import math


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