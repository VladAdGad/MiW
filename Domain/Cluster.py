import numpy

from Domain import Utility


class Cluster:
    distances = numpy.array([])

    def __init__(self, coordinates, name):
        self.coordinates = coordinates
        self.name = name

    def set_distances(self, *list_of_coordinates):
        for coordinates in list_of_coordinates:
            self.distances = numpy.append(self.distances, Utility.calc_distance(coordinates, self.coordinates))
