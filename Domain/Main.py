from Domain import Centroid, Iris
import csv
import numpy as np


def distance(coordinates_1, coordinates_2):
    return np.math.sqrt(
        (coordinates_1[0] - coordinates_2[0]) ** 2 +
        (coordinates_1[1] - coordinates_2[1]) ** 2 +
        (coordinates_1[2] - coordinates_2[2]) ** 2 +
        (coordinates_1[3] - coordinates_2[3]) ** 2)


Iris_setosa = Centroid.Centroid(np.array([5.0060, 3.4180, 1.4640, 0.2440], dtype=float), "Iris-setosa")
Iris_versicolor = Centroid.Centroid(np.array([5.9360, 2.7700, 4.2600, 1.3260], dtype=float), "Iris-versicolor")
Iris_virginica = Centroid.Centroid(np.array([6.5880, 2.9740, 5.5520, 2.0260], dtype=float), "Iris-virginica")
Centroids = (Iris_setosa, Iris_versicolor)

with open("../Resources/iris.txt", "r") as file:
    lines = csv.reader(file, delimiter=",")
    for line in lines:
        cur_iris = Iris.Iris(np.array((line[0], line[1], line[2], line[3]), dtype=float), line[4])
        min_distance = distance(Centroids[0].coordinates, cur_iris.coordinates)
        target_centroid = Centroids[0]
        for centroid in Centroids:
            cur_distance = distance(centroid.coordinates, cur_iris.coordinates)
            if min_distance > cur_distance:
                min_distance = cur_distance
                target_centroid = centroid
