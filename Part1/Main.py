import pandas as pd

from Cluster import Cluster
from Iris import Iris
from Universe import Univervse

irises = pd.read_csv('../Resources/iris.txt', sep=',', header=None)
irises.columns = ['x1', 'y1', 'x2', 'y2', 'name']

clusters_names = irises.name.unique()

irises_ = [Iris(row['x1'], row['y1'], row['x2'], row['y2'], row['name']) for _, row in irises.iterrows()]

cluster_1 = Cluster()
cluster_2 = Cluster()
cluster_3 = Cluster()

for element in irises_:

    if element.name == clusters_names[0]:
        cluster_1.add(element)

    if element.name == clusters_names[1]:
        cluster_2.add(element)

    if element.name == clusters_names[2]:
        cluster_3.add(element)

universe = Univervse([cluster_1, cluster_2, cluster_3])

x_1, y_1, x_2, y_2 = 0., 0., 0., 0.
name = None
count = -1.
for element in universe.clusters:
    if count == -1:
        count = element.count
    for iris in element.iris_cluster:
        y_1 += iris.y1
        x_1 += iris.x1
        x_2 += iris.x2
        y_2 += iris.y2
        if name is None:
            name = iris.name
    print('{0}'.format(name) + ' ({0})'.format(count) + ' x:1 {:.4f}'.format(x_1 / count) + ' y:1 {:.4f}'.format(
        y_1 / count) + ' x:2 {:.4f}'.format(x_2 / count) + ' y:2 {:.4f}'.format(y_2 / count))
    x_1, y_1, x_2, y_2 = 0., 0., 0., 0.
    name = None
    count = -1
