import csv
import math
import sys

import enum

eps = float(sys.argv[1])


class Type(enum.Enum):
    LOW = "LOW"
    HIGH = "HIGH"


class Iris:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.n_type = None
        self.distances = dict()

    def compare_dist_cluster(self, clusters):
        distances = [self._calc_distance(cluster.cluster) for cluster in clusters]
        r_min = min(distances)
        r_q = r_min * eps
        rq_list = [1 for k in self.distances if self.distances[k] <= r_q]
        if len(rq_list) > 1:
            self.n_type = Type.HIGH
        else:
            self.n_type = Type.LOW

    def _calc_distance(self, cluster):

        x = (self.a - cluster.a) ** 2 \
            + (self.b - cluster.b) ** 2 \
            + (self.c - cluster.c) ** 2 \
            + (self.d - cluster.d) ** 2
        dist = round(math.sqrt(x), 2)
        self.distances[cluster] = dist
        return dist

    def __str__(self):
        return "[{},{},{},{}] -> {}".format(self.a, self.b, self.c, self.d, self.n_type)


class Centroid:

    def __init__(self, cluster, category_name):
        self.cluster = cluster
        self.category_name = category_name
        self.low_nodes = list()
        self.high_nodes = list()

    def __str__(self):
        return "{}({}){}".format(self.category_name, len(self.nodes), str(self.centroid))


setosa_cluster = Centroid(Iris(5.01, 3.42, 1.46, 0.24), "Iris setosa")
viriginica_cluster = Centroid(Iris(6.59, 2.97, 5.55, 2.03), "Iris virginica")
versicolor_cluster = Centroid(Iris(5.94, 2.77, 4.26, 1.33), "Iris versicolor")


def read_file(fileTxt):
    with open(fileTxt, "r") as csvfile:
        csv_data = csv.reader(csvfile, delimiter=",")
        for row in csv_data:
            if not row:
                continue
            a = float(row[0])
            b = float(row[1])
            c = float(row[2])
            d = float(row[3])
            node = Iris(a, b, c, d)
            node.compare_dist_cluster([setosa_cluster, viriginica_cluster, versicolor_cluster])
            print(node)


if __name__ == '__main__':
    read_file("../Resources/iris.txt")
