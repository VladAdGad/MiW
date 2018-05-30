import math

import distance as distance
from scipy.spatial import distance

class Centroid:

    def __init__(self, coordinates, category_name):
        self.coordinates = coordinates
        self.category_name = category_name
        self.low_approximation = ()
        self.high_low_approximation = ()

    def compare_dist_cluster(self, clusters, epsilon):
        distances = [self._calc_distance(cluster.cluster) for cluster in clusters]
        r_min = min(distances)
        r_q = r_min * epsilon
        rq_list = [1 for k in self.distances if self.distances[k] <= r_q]
        if len(rq_list) > 1:
            self.n_type = Type.HIGH
        else:
            self.n_type = Type.LOW

    def __str__(self):
        return "Coordinates: {}, Name: {}".format(self.coordinates, self.category_name)
