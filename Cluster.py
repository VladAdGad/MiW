
class Cluster():
    def __init__(self, iris_cluster=None, count=0):
        if iris_cluster is None:
            iris_cluster = []
        self.iris_cluster = iris_cluster
        self.count = count


    def add(self, iris):
        self.iris_cluster.append(iris)
        self.count += 1
