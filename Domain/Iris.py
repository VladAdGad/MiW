import numpy

from Domain import Utility


class Iris:
    distances = numpy.array([])

    def __init__(self, coordinates, name):
        self.coordinates = coordinates
        self.name = name

    def set_distances(self, l1, l2, l3):
        self.distances = numpy.append(self.distances, Utility.calc_distance(l1, self.coordinates))
        self.distances = numpy.append(self.distances, Utility.calc_distance(l2, self.coordinates))
        self.distances = numpy.append(self.distances, Utility.calc_distance(l3, self.coordinates))
