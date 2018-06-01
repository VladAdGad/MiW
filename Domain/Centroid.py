import numpy
from statistics import mean


class Centroid:
    low_approximation = numpy.array([])
    high_approximation = numpy.array([])
    clusters = numpy.array([])
    all_clusters = set()

    def __init__(self, coordinates, category_name):
        self.coordinates = coordinates
        self.category_name = category_name
        self.all_clusters.add(self)

    def approximate(self, distances, epsilon):
        search_dist = min(distances) * epsilon
        count = [0 for dist in distances if dist <= search_dist]
        if len(count) > 1:
            self.high_approximation = numpy.append(self.high_approximation, 1)
        else:
            self.low_approximation = numpy.append(self.low_approximation, 0)

    def add_cluster(self, cluster):
        self.clusters = numpy.append(self.clusters, cluster)

    def calc_quality(self):
        isolation = sum(node.distance(c) for c in self.all_clusters for node in self.clusters if c != self)
        s = sum(node.distance(self) for node in self.clusters)
        return round(isolation / s, 2)

    def recalc_centroid(self):
        self.coordinates[0] = round(mean([cluster.coordinates[0] for cluster in self.clusters]), 2)
        self.coordinates[1] = round(mean([cluster.coordinates[1] for cluster in self.clusters]), 2)
        self.coordinates[2] = round(mean([cluster.coordinates[2] for cluster in self.clusters]), 2)
        self.coordinates[3] = round(mean([cluster.coordinates[3] for cluster in self.clusters]), 2)

    def __str__(self):
        return "Coordinates: {}, Name: {}".format(self.coordinates, self.category_name)
