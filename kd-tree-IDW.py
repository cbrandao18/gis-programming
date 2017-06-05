#Christie Brandao
#kd tree idw class exercise

#Q1
#G will be tested using the update_neighbors because it might be in the red
#circle since a little portion of the box is in the circle.

#Q2
import sys
sys.path.append('C:\Users\Christie\Documents\OSU\Fall2016\GEOG_5222_GIS_PROGRAMING')
from math import sqrt

from geom.point import *
from interpolation.idw import *
from interpolation.prepare_interpolation_data import *

def IDW(Z, b):
    zw = 0.0                # sum of weighted z
    sw = 0.0                # sum of weights
    N = len(Z)              # number of points in the data
    for i in range(N):
        d = Z[i][3]
        if d == 0:
            return Z[i][2]
        w = 1.0/d**b
        sw += w
        zw += w*Z[i][2]
    return zw/sw

def prepare_interpolation_data(x, Z, N=10):
    vals = [z[2] for z in Z]
    mu = sum(vals)/len(vals)
    dist = [sqrt((z[0]-x.x)**2 + (z[1]-x.y)**2) for z in Z]
    Z1 = [(Z[i][0], Z[i][1], Z[i][2], dist[i]) for i in range(len(dist))]
    Z1.sort(key=lambda Z1: Z1[3])
    Z1 = Z1[:N]
    return Z1, mu


fname = 'C:\Users\Christie\Documents\OSU\Fall2016\GEOG_5222_GIS_PROGRAMING\kdtree-idw'
f = open(fname, 'r')
Z = f.readlines()
Z = [x.strip().split() for x in Z]
Z = [ [ float(x[0]),float(x[1]),float(x[2])] for x in Z]

x = Point(337000, 4440911)
N = 10

Z1 = prepare_interpolation_data(x, Z, N)[0]
Z2 = [[z[0].x, z[0].y, z[0].key, z[1]] for z in Z2]

print 'power=0.0:', IDW(Z1, 0)
print 'power=0.5:', IDW(Z1, 0.5)
print 'power=1.0:', IDW(Z1, 1.0)
print 'power=1.5:', IDW(Z1, 1.5)
print 'power=2.0:', IDW(Z1, 2.0)
print 'power=0.0:', IDW(Z2, 0)
