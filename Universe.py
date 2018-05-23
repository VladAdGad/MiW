class Univervse:
    def __init__(self, clasters=None):
        if clasters is None:
            clasters = []
        self.clusters = clasters

    def add(self, cluster):
        self.clusters.append(cluster)

