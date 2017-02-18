import math
import matplotlib.pyplot as plt

def show(points):
        plt.scatter([xy.x for xy in points],
                    [xy.y for xy in points])
        plt.axis('equal')
        plt.show()

class XY:
    def __init__(self, x, y):
        self.nums = [x,y]

    @property
    def x(self):
        return self.nums[0]

    @property
    def y(self):
        return self.nums[1]

    @property
    def r(self):
        return math.sqrt(self.x*self.x + self.y*self.y)

    @property
    def theta(self):
        '''returns angle of the point in radians'''
        try:
            adjust = 0 #how much to adjust the angle (radians)
            if (self.x < 0 and self.y >= 0) or (self.x < 0 and self.y <= 0): #2nd quadrant
                adjust = math.pi
            elif (self.x > 0 and self.y < 0):
                adjust = 2*math.pi
            return adjust + math.atan(self.y/self.x)
        except ZeroDivisionError:
            if self.y == 0:
                return null
            elif self.y > 0:
                return math.pi/2
            else:
                return (3*math.pi/2)


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

# a = Reg_Polygon(1864)
# for i in range(1865, 1910):
#     print(len(a.vertices))
#     a = a + Reg_Polygon(i)
#     a.sort()
#a = Reg_Polygon(4)
#b = Reg_Polygon(5)