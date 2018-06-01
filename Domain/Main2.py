import csv, sys
import math
import enum
import random

from statistics import mean


class Cluster:
    all = set()

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.nodes = set()
        Cluster.all.add(self)

    def calc_dist(self, n):
        return round(math.pow((self.a - n.a), 2) + \
                     math.pow((self.b - n.b), 2) + \
                     math.pow((self.c - n.c), 2) + \
                     math.pow((self.d - n.d), 2))

    def __str__(self):
        return "[{},{},{},{}]".format(self.a, self.b, self.c, self.d)


class Centroid:
    all_clusters = set()

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.clusters = list()
        self.all_clusters.add(self)

    def add(self, node):
        self.clusters.append(node)

    def recalc_centroid(self):
        self.a = round(mean([n.a for n in self.clusters]), 2)
        self.b = round(mean([n.b for n in self.clusters]), 2)
        self.c = round(mean([n.c for n in self.clusters]), 2)
        self.d = round(mean([n.d for n in self.clusters]), 2)

    def calc_Q(self):
        isolation = sum(node.distance(c) for c in self.all_clusters for node in self.clusters if c != self)
        s = sum(node.distance(self) for node in self.clusters)
        return round(isolation / s, 2)

    def __str__(self):
        return "{} {} {} {}".format(self.a, self.b, self.c, self.d)


def readFile(file):
    with open(file, "r") as csvfile:
        csv_data = csv.reader(csvfile, delimiter=",")
        for row in csv_data:
            if not row:
                continue
            a = float(row[0])
            b = float(row[1])
            c = float(row[2])
            d = float(row[3])
            node = Cluster(a, b, c, d)
            yield node


if __name__ == '__main__':
    nodes = list(readFile("iris.txt"))
    c1 = Centroid(5.01, 3.42, 1.46, 0.24)
    c2 = Centroid(6.59, 2.97, 5.55, 2.03)
    c3 = Centroid(5.94, 2.77, 4.26, 1.33)
    cluster_q = dict()
    # assignment
    for node in nodes:
        distances = {}
        distances[node.calc_dist(c1)] = c1
        distances[node.calc_dist(c2)] = c2
        distances[node.calc_dist(c3)] = c3
        distances[min(distances.keys())].add(node)
    cluster_q[c1] = c1.calc_Q()
    cluster_q[c2] = c2.calc_Q()
    cluster_q[c3] = c3.calc_Q()
    c1.recalc_centroid()
    c2.recalc_centroid()
    c3.recalc_centroid()
    c1_q = c1.calc_Q()
    c2_q = c2.calc_Q()
    c3_q = c3.calc_Q()
    while cluster_q[c1] < c1_q or cluster_q[c2] < c2_q or cluster_q[c3] < c3_q:
        cluster_q[c1] = c1_q
        cluster_q[c2] = c2_q
        cluster_q[c3] = c3_q
        c1.recalc_centroid()
        c2.recalc_centroid()
        c3.recalc_centroid()
        c1_q = c1.calc_Q()
        c2_q = c2.calc_Q()
        c3_q = c3.calc_Q()
    for c in cluster_q:
        print(c)
