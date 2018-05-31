import math


def calc_distance(coordinates_1, coordinates_2):
    return math.sqrt(
        (coordinates_1[0] - coordinates_2[0]) ** 2 +
        (coordinates_1[1] - coordinates_2[1]) ** 2 +
        (coordinates_1[2] - coordinates_2[2]) ** 2 +
        (coordinates_1[3] - coordinates_2[3]) ** 2)
