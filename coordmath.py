import math

class DistCalc:

    def __init__(self):
        print 'we rolling'
        pass

    def calculate(point1, point2):
        latDiff = point1.lat.degrees_full - point2.lat.degrees_full
        longDiff = point1.long.degrees_full - point2.long.degrees_full

        print 'latDiff:', latDiff
        print 'longDiff:', longDiff

class PointSet:
    def __init__(self):
        self.points = []

    # def cleanPoints(self):
    #     for i in range(0, len(self.points)):
    #         x = self.points[i]
            
    #         if isinstance(x, Point):
    #             pass
    #         elif isinstance(x, list):
    #             x = Point(x)
                
    #         elif isinstance(x, str):
    #             x = Point(x)

    #         self.points[i] = x    

    def add(self, inputObj):
        
        if isinstance(inputObj, Point):
            self.points.append(inputObj)
        else:
            newPoint = Point(coords)
            self.points.append(newPoint)

    def delete(index):
        self.points.pop(index)

    # def list(self):
    #     print point for point in self.points


class Point:
    def __init__(self, pStr):
        #assume it's a string for now: '0.0 N, 0.0 E'
        #initialize coords as 0 N, 0 E?

        self.pStr = pStr
        self.to_s = pStr

        p = self.pStr.split(', ')
        self.lat_str = p[0]
        self.long_str = p[1]

        self.lat_deg = Coord(self.long_str)
        self.long_deg = Coord(self.lat_str)

        # self.lat_rad = math.radians(self.lat_deg)
        # self.long_rad = math.radians(self.long_deg)

        # self.multiplier = math.cos(self.lat.deg_dec)
        # this is for calculating length of a degree at the given latitude

class Coord:
    def __init__(self, c='0 N'):
        [magnitude,direction] = c.split(' ')

        self.magnitude = float(magnitude) #handle deg/min/sec later
        self.direction = Dir(direction)

        # if self.magnitude < 0:
        #     self.magnitude = -self.magnitude #add a flip() method later
        #     self.direction.flip()

    # def __init__(self, degrees, minutes=0, seconds=0):
        
    #     self.degrees = degrees
    #     self.minutes = minutes
    #     self.seconds = seconds

    #     self.to_dec = float(degrees) + (float(minutes)/60.0) + (float(seconds)/3600.0)
    #     #self.to_s = 

class Dir:
    #direction: 1=N, 2=E, 3=S, 4=W, 0=unassigned

    def __init__(self, d):
        if d.upper() in ['N', 'E', 'S', 'W']:
            self.to_s = d.upper()

            if self.to_s == 'N':
                self.to_i = 1
            elif self.to_s == 'E':
                self.to_i = 2
            elif self.to_s == 'S':
                self.to_i = 3
            elif self.to_s == 'W':
                self.to_i = 4
            else:
                pass #shouldn't happen, already filtered for NESW
        
        elif d in ['0', '1', '2', '3', '4']:
            self.to_i = d
            
            if d == 0:
                self.to_s = '-'
            elif d == 1:
                self.to_s = 'N'
            elif d == 2:
                self.to_s = 'E'
            elif d == 3:
                self.to_s = 'S'
            elif d == 4:
                self.to_s = 'W'
            else:
                pass #shouldn't happen, already filtered for 0-4

        else:
            pass #invalid input, handle later
        
    def flip(self):

        if self.to_i == 0:
            pass #nothing to flip if there's no direction

        elif self.to_i == 1:
            self.to_i = 3
            self.to_s = 'S'

        elif self.to_i == 2:
            self.to_i = 4
            self.to_s = 'W'

        elif self.to_i == 3:
            self.to_i = 'N'
            self.to_s = 1

        elif self.to_i == 4:
            self.to_i = 2
            self.to_s = 'E'







