#Christie Brandao
#kd-tree-coding exercise

#Q1
#We are able to alternate between X and Y coordinates in the kdcompare function
#because it returns the branch (either right or left) so the x and y doesn't matter, just what branch it is on.

#Q2
# To stop the recursive call, the returned branch from kdcompare < 0 stops the call
# as well as if_find_only is false and the child is None.

#Q3
# The list of points is changed after kdtree2 because the points list is sorted using
# points.sort() through the lambda function.

#Q4
import copy
import sys
sys.path.append('C:\Users\Christie\Documents\OSU\Fall2016\GEOG_5222_GIS_PROGRAMING')

from geom.point import *
from indexing.kdtree1 import *
from indexing.bst import *

data1 = [ (2,2), (0,5), (8,0), (9,8), (7,14), (13,12), (14,13) ]
points = [Point(d[0], d[1]) for d in data1]
points0 = copy.deepcopy(points)

t1 = kdtree(points)
bt_print(t1)
#bt_print prints out the points in ascending order of the X point

#Q5
points2 = [(2.0, 2.0), (0.0, 5.0), (8.0, 0.0), (9.0, 8.0), (7.0, 14.0), (13.0, 12.0), (14.0, 13.0)]
t2 = kdtree2(points2)
tree_print(t2)
#No it's not the 3rd point entered in the tree because the nodes on the left are created first. 4 points are entered first 

#Q6
# It works because it recursively finds the height of the left-most node and then the right-most node and takes the larger of the two
# which is the max height of the tree. 
