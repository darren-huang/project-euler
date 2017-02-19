import math
import matplotlib.pyplot as plt

def show(points):
        plt.scatter([xy.x for xy in points],
                    [xy.y for xy in points])
        plt.axis('equal')
        plt.show()

class XY:
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy

        try: #theta = angle of the point in radians WITH respect to positive x axis
            adjust = 0 #how much to adjust the angle (radians)
            if (self.x < 0 and self.y >= 0) or (self.x < 0 and self.y <= 0): #2nd quadrant
                adjust = math.pi
            elif (self.x > 0 and self.y < 0):
                adjust = 2*math.pi
            self.theta = adjust + math.atan(self.y/self.x)
        except ZeroDivisionError:
            if self.y == 0:
                self.theta = null
            elif self.y > 0:
                self.theta = math.pi/2
            else:
                self.theta = (3*math.pi/2)

    @property
    def theta_ry(self):
        angle = self.theta - math.pi/2
        if angle < 0:
            angle += 2*math.pi
        return angle

    def __add__(self, xy):
        return XY(xy.x + self.x, xy.y + self.y)

    def __sub__(self, xy):
        return XY(self.x - xy.x, self.y - xy.y)

    def __repr__(self):
        return "({},{})".format(str(self.x),str(self.y))



class Shape:
    def __init__(self):
        self.sides = [] #represented by vecotrs
        self.first_vertex = None #where the first vector corresponds to

    def __add__(self, shape2): #shape sides are sorted by theta!
        a = Shape() #a stands for answer
        a.first_vertex = self.first_vertex + shape2.first_vertex
        i1, i2 = 0, 0
        i1max, i2max = len(self.sides), len(shape2.sides)

        while (i1 < i1max) and (i2 < i2max):
            if self.sides[i1].theta_ry == shape2.sides[i2].theta_ry:
                a.sides.append(self.sides[i1] + shape2.sides[i2])
                i1 += 1
                i2 += 1
            elif self.sides[i1].theta_ry < shape2.sides[i2].theta_ry:
                a.sides.append(self.sides[i1])
                i1 += 1
            else:
                a.sides.append(shape2.sides[i2])
                i2 += 1
        if (i1 < i1max):
            for i in range(i1, i1max):
                a.sides.append(self.sides[i])
        elif (i2 < i2max):
            for i in range(i2, i2max):
                a.sides.append(shape2.sides[i])
        return a











    #ADD FUCNTION DOES NOT WORK ##########################################################################
    #v1 with adjacent points (theta is really really close) without v2 points inside will make some points
    #left out of the resulting "answer" vertices
    
    ######################################################################################################
  #   def __add__(self, shape): #SHAPES MUST BE SORTED BY THETA
        # answer = Shape()
        # v1 = self.vertices
        # v2 = shape.vertices
        # if v1[0].theta > v2[0].theta:
        #     v1,v2 = v2,v1
        # i2 = 0
        # for i1 in range(len(v1) - 1): #checks all 2 adjacent vertices of v1
        #     while i2 < len(v2) and v1[i1].theta <= v2[i2].theta < v1[i1 + 1].theta: 
        #         #appends the addition of vertices of 'shape' between the 2 self vertices
        #         answer.vertices.append(v1[i1] + v2[i2])
        #         answer.vertices.append(v1[i1 + 1] + v2[i2])
        #         i2 += 1
        # i1 = len(v1) - 1
        # #need to check last vertex and first vertex
        # while i2 < len(v2) and (v1[i1].theta <= v2[i2].theta <= 0): 
        #     #appends the addition of vertices of 'shape' between the 2 self vertices
        #     answer.vertices.append(v1[i1] + v2[i2])
        #     answer.vertices.append(v1[0] + v2[i2])
        #     i2 += 1
        # return answer
    #######################################################################################################

    def sort(shape):
        shape.vertices.sort(key = lambda xy: xy.theta)

    def show(self):
        points = [self.first_vertex]
        for side in self.sides:
            points.append(points[-1] + side)
        show(points)



class Reg_Polygon(Shape):
    def __init__(self, n):
        Shape.__init__(self)
        v = [] #vertices
        for k in range(n):
            v.append(XY(math.cos(math.radians( \
                                    ((2*k - 1) / n)*180)),
                                    math.sin(math.radians( \
                                    ((2*k - 1) / n)*180))))
        v.append(v[0])
        self.first_vertex = v[0]
        for i in range(len(v) - 1):
            self.sides.append(v[i + 1] - v[i])

# def add_vertices(shape1, shape2):
#     answer = []
#     for v1 in shape1.vertices:
#         for v2 in shape2.vertices:
#             answer.append(XY(v1.x + v2.x, v1.y + v2.y))
#     return answer

def test_theta(x,y):
    return math.degrees(XY(x, y).theta)

def test_theta_ry(x,y):
    return math.degrees(XY(x, y).theta_ry)

a = Reg_Polygon(1864)
for i in range(1865, 1910):
    a = a + Reg_Polygon(i)
    print(len(a.sides))
#     a.sort()
#a = Reg_Polygon(4)
#b = Reg_Polygon(5)