import sys
from geom.point import *

#Generating list of points from (0,0) to (4,4)
list_of_points = []
i = 0
j = 0
while i < 5:
    while j < 5:
        point = Point(i, j)
        list_of_points.append(point)
        j = j + 1
    i = i + 1
    j = 0

print list_of_points
