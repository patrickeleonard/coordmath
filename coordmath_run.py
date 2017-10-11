from distcalc import DistCalc, PointSet, Point, Coord
import math


a = Point('47.6062 N, 122.3321 W') #Seattle
b = Point('41.8781 N, 87.6298 W') #Chicago

pointSet = PointSet()

pointSet.add(a)
pointSet.add(b)

for point in pointSet.points:
    print point.to_s

# DistCalc.calculate(a,b)