import csv
import numpy as np
from Domain import Utility
from Domain.Centroid import Centroid
from Domain.Iris import Iris

centroid_1 = Centroid(np.array([5.006, 3.418, 1.464, 0.244], dtype=float), "Iris-setosa")
centroid_2 = Centroid(np.array([5.936, 2.77, 4.26, 1.326], dtype=float), "Iris-versicolor")
centroid_3 = Centroid(np.array([6.588, 2.974, 5.552, 2.026], dtype=float), "Iris-virginica")
centroids = (centroid_1, centroid_2, centroid_3)

with open("../Resources/iris.txt", "r") as file:
    lines = csv.reader(file, delimiter=",")
    for line in lines:
        cur_iris = Iris(np.array((line[0], line[1], line[2], line[3]), dtype=float), line[4])
        cur_iris.set_distances(centroids[0].coordinates, centroids[1].coordinates, centroids[2].coordinates)
        min_distance = Utility.calc_distance(centroids[0].coordinates, cur_iris.coordinates)
        target_centroid = centroids[0]
        for centroid in centroids:
            cur_distance = Utility.calc_distance(centroid.coordinates, cur_iris.coordinates)
            if min_distance > cur_distance:
                min_distance = cur_distance
                target_centroid = centroid
        target_centroid.approximate(cur_iris.distances, 1)

for centroid in centroids:
    print(len(centroid.high_approximation))
    print(len(centroid.low_approximation))
