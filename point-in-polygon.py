import sys
sys.path.append("C:\\brandao")
from geom.point import *
from geom.point_in_polygon import *
import matplotlib.pyplot as plt

triangle = [Point(p[0], p[1]) for p in [ [0,0], [10,5], [5,10], [0,0] ]]
inout = lambda x: 1 if x is True else 0
bounds = [[0,0], [10,0], [10,10], [0,0]]
import random
points = [Point(random.random()*10, random.random()*10) for i in range(100)]
num_in = 0
for p in points:
    num_in += inout(pip_cross(p, triangle)[0])

print num_in
from geom.centroid import *
print centroid(triangle)[0]

line1 = [ [p.x, p.y] for p in triangle ]
l1 = plt.Polygon(line1, closed=True, fill=True, facecolor='#AAAAAA', edgecolor='none', alpha=0.5)
plt.gca().add_patch(l1)
l3 = plt.scatter([p.x for p in points], [p.y for p in points], color='red', s=15)
plt.axis('equal')
plt.show()

def count_in_triangle(points, triangle):
    num_in = 0
    for p in points:
        num_in += inout(pip_cross(p, triangle)[0])
    return num_in

print count_in_triangle(points, triangle)
counts=[]
for i in range(500):
    points = [Point(random.random()*10, random.random()*10) for i in range(100) ]
    counts.append(count_in_triangle(points, triangle))

from numpy import median
print min(counts), max(counts), median(counts), sum(counts)/float(len(counts))

#Histogram
plt.hist(counts, 10, normed=1, facecolor='grey', alpha=0.75)
plt.show()
