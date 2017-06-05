'''
Christie Brandao
'''

#Q1
import sys

from geom.point import *
from indexing.kdtree1 import *
from indexing.kdtree3 import *
from indexing.bst import *
import random
import time
from interpolation.idw import *
from interpolation.prepare_interpolation_data import *
from math import sqrt

data = [Point(random.randint(0, 30), random.randint(0,30)) for i in range (100)]
tree = kdtree2(data)
p = Point(14,18)
n = 3
nearests = []

time1 = time.time()
# computation starts here
for i in range(100000000):
    pass
nnquery(tree, p, n, nearests)
# computation done
time2 = time.time()
print 'using a k-D tree, the time to get the neighboring points is', time2-time1, 'seconds'

fname = 'C:\Users\Christie\Documents\OSU\Fall2016\GEOG_5222_GIS_PROGRAMING\data\\necoldem.dat'
f = open(fname, 'r')
Z = f.readlines()
Z = [x.strip().split() for x in Z]
Z = [ [ float(x[0]),float(x[1]),float(x[2])] for x in Z]

x = Point(337000, 4440911)
N = 10

Z1 = prepare_interpolation_data(x, Z, N)[0]
time3 = time.time()
# computation starts here
for i in range(100000000):
    pass
IDW(Z1, 0)
# computation done
time4 = time.time()
print 'without using a k-D tree, the time using IDW function is', time4-time3, 'seconds'

#Q2
'''
IDW's calculation values for unknown points are more
accurate when more known points are entered. This is because it assumes things closers together are more
alike than things farther apart so the more known points you have, the more accurate the unknown values
are going to be. 
'''

#Q3
'''
The order of points printed out by bt_print is correct becasue it is recursively calling the left
most branch until reaching the leaf and printing it. If there are no left branches, it does the
same with the right branch.

bt creates the tree correctly but is inefficient because it takes the first value as the root node
but this is not ideal because there is no guanratee of a balanced tree.

The problem with indexing points through trees in 2D space is that the time it takes to run the
function is based on the height of the tree which could be large since it is not guaranteed that
the tree is balanced.
'''

#Q4
def kdtreeleft(points):
    root = kDTreeNode(point=points[0], left=None, right=None)
    for p in points[1:]:
        node = kDTreeNode(point=p, left=None, right=None)
        p0, lr = query_kdtree(root, p, 0, False)
        if lr<0:
            p0.left = node
    return root
#Q5
def insert_pqtree_se(q, p):
    n = search_pqtree(q, p, False)
    node = PQuadTreeNode(point=p)
    n.se = node
    
