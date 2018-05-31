class Centroid:

    def __init__(self, coordinates, category_name):
        self.coordinates = coordinates
        self.category_name = category_name
        self.low_approximation = list()
        self.high_approximation = list()

    def approximate(self, distances, epsilon):
        search_dist = min(distances) * epsilon
        count = 0
        for dist in distances:
            if dist <= search_dist:
                count += 1
        if count > 1:
            self.high_approximation.append(1)
        else:
            self.low_approximation.append(0)

    def __str__(self):
        return "Coordinates: {}, Name: {}".format(self.coordinates, self.category_name)
