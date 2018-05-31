import numpy as np


class Iris:
    distances = np.array([])

    def __init__(self, coordinates, name):
        self.coordinates = coordinates
        self.name = name

    def set_distances(self, l1, l2, l3):
        self.distances = np.append(self.distances, self.calc_distance(l1, self.coordinates))
        self.distances = np.append(self.distances, self.calc_distance(l2, self.coordinates))
        self.distances = np.append(self.distances, self.calc_distance(l3, self.coordinates))

    @staticmethod
    def calc_distance(coordinates_1, coordinates_2):
        return np.math.sqrt(
            (coordinates_1[0] - coordinates_2[0]) ** 2 +
            (coordinates_1[1] - coordinates_2[1]) ** 2 +
            (coordinates_1[2] - coordinates_2[2]) ** 2 +
            (coordinates_1[3] - coordinates_2[3]) ** 2)
