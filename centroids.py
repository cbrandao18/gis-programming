import matplotlib.pyplot as plt

import sys
from geom.point import *
from geom.centroid import *

points = [ [1,1], [4,3], [8,3], [8,3.5], [4,3.5], [1,5], [1,1] ]

polygon = [ Point(p[0], p[1]) for p in points ]
c = centroid(polygon)[1]

# TODO: compute the mean of the X coordinates in polygon as x
x_coords = [p.x for p in polygon]
mean_x = 0
sum_x = 0
for i in range(x_coords):
    sum_x = sum_x + x_coords[i]
mean_x = sum_x / len(x_coords)

# TODO: compute the mean of the X coordinates in polygon as y
y_coord = [p.y for p in polygon]
mean_y = 0
sum_y = 0
for j in range(y_coords):
    sum_y = sum_y + y_coords[j]
mean_y = sum_y / len(y_coords)

d = Point(x, y)
print c, d

n = len(polygon)
line1 = [ [p.x, p.y] for p in polygon ]
l1 = plt.Polygon(line1, closed=True, fill=True, facecolor='grey', edgecolor='blue', alpha=0.5)
plt.gca().add_patch(l1)
plt.scatter([c.x], [c.y], color='blue', alpha=.9)
plt.scatter([d.x], [d.y], color='red', alpha=.9)

plt.text(c.x+0.1, c.y+0.1, 'centroid')
plt.text(d.x+0.1, d.y-0.2, 'mean')
plt.axis('equal')
plt.show()
