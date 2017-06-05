import matplotlib.pyplot as plt

import sys
from geom.point import *
from geom.centroid import *

points = [ [1,1], [1,2], [1,3], [1,4], [1,5], [2,5], [2,4], [2,3], [2,2], [3,2], [4,2], [5,2], [5,1], [4,1], [3,1], [2,1], [1,1] ]
polygon = [ Point(p[0], p[1]) for p in points ]
c = centroid(polygon)[1]


n = len(polygon)
line1 = [ [p.x, p.y] for p in polygon ]
l1 = plt.Polygon(line1, closed=True, fill=True, facecolor='grey', edgecolor='blue', alpha=0.5)
plt.gca().add_patch(l1)

plt.text(c.x+0.1, c.y+0.1, 'centroid')
plt.axis('equal')
plt.show()
