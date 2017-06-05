#Christie Brandao

#Q1 - Equirectangular projection
import sys
sys.path.append('C:\\brandao')
from geom.worldmap import *
from numpy import cos, radians, pi
import matplotlib.pyplot as plt

fname = 'C:\\brandao\\coastlines\\ne_110m_coastline.shp'
raw_points, numgraticule, numline = prep_projection_data(fname)

def plot_world(points, numgraticule, numline):
    ax = plt.gca()
    for i in range(numline):
        if i<numgraticule:
            col = 'lightgrey'
        else:
            col = '#5a5a5a'
        pts = [[p[1], p[2]] for p in points if p[0]==i]
        l = plt.Polygon(pts, color=col, fill=False, closed=False)
        ax.add_line(l)

    plt.axis('equal')
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    plt.show()

def transform_equirectangular(lon, lat, lat0=0):
    x = lon * cos(radians(lat0))
    y = lat
    return x, y


from geom.transforms import transform_equirectangular

points=[]
for p in raw_points:
    p1 = transform_equirectangular(p[1], p[2])
    points.append([p[0], p1[0], p1[1]])

plot_world(points, numgraticule, numline)

#Q2
from geom.point import *
from geom.point_in_polygon import *
import matplotlib.pyplot as plt
import random
from osgeo import ogr
fname = raw_input("Enter location of shapefile: ")
driver = ogr.GetDriverByName(fname)
vector = driver.Open(fname, 0)
layer = vector.GetLayer(0)
boundingbox = geom.getEnvelope()
polygon_ref = geom.GetGeometryRef(0)
polygon = []
for point in polygon_ref.GetPointCount():
    polygon[point] = Point(polygon_ref.GetPoint(point)[0], polygon_ref.GetPoint(point)[1])


inout = lambda x: 1 if x is True else 0
rand_points = [Point(random.random()*10, random.random()*10) for i in range(500
                                                                            )]
def count_in_polygon(rand_points, polygon):
    num_in = 0
    for p in rand_points:
        num_in += inout(pip_cross(p, polygon)[0])
    return num_in

counts=[]
for i in range(100):
    points = [Point(random.random()*10, random.random()*10) for i in range(500) ]
    counts.append(count_in_polygon(points, polygon))

#Histogram
plt.hist(counts, 10, normed=1, facecolor='grey', alpha=0.75)
plt.show()

#Q3
# This computes the intersection point by already checking earlier in the program if the lines intersect at all and then uses
# Line 1 (x1, y1) and (x2, y2) endpoints with Line 2 having (x3, y3) and (x4, y4). The calculation used for the x coordinate
# is (Line1 Slope * x1) - (Line2 slope * x3) + y3 - y1 / (Line1 Slope - Line2 Slope) which directly is translated in the code.

#Q4
# pip_cross provides a consistent treatment of the points that are on the boundary as it does count the point inside the
# polygon. This is because if the x coordinate of the intersection point is >= x than it is counted (is_point_inside is set
# to 'not False' which means True. If it was just > x then a point on the border would not be counted.

#Q5
# lon0 represents the central meridian in degrees which runs down the center of the map to make it symmetrical (not the
# points displayed on the map are symmetrical, just the shape of the globe). Naturally, since the central meridian is at
# the center of the map, it is 0 degrees and changing the central meridian degrees changes the longitude since it uses
# lon1 = lon - lon0 as an equation based on the central meridian. If the central meridian is not in the center anymore,
# you will achieve an asymmetrical map.

#Q6
# With the Robinson projecttion, the central meridian is represented as a straight line that is 0.5072 as long as the equator
# which is why y coordinate is using 0.5072 in its equation. x is calculated by dividing it by 360 degrees and then multiplying
# by the longitude. 
