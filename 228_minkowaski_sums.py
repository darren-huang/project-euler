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

	def __add__(self, xy):
		return XY(xy.x + self.x, xy.y + self.y)

	def __repr__(self):
		return "({},{})".format(str(self.x),str(self.y))



class Shape:
	def __init__(self):
		self.vertices = []

	@property
	def sides(self):
		return len(self.vertices)

class Reg_Polygon(Shape):
	def __init__(self, n):
		Shape.__init__(self)
		for k in range(1, n+1):
			self.vertices.append(XY(math.cos(math.radians( \
									((2*k - 1) / n)*180)),
									math.sin(math.radians( \
									((2*k - 1) / n)*180))))

	def show(self):
		show(self.vertices)



def add_vertices(shape1, shape2):
	answer = []
	for v1 in shape1.vertices:
		for v2 in shape2.vertices:
			answer.append(XY(v1.x + v2.x, v1.y + v2.y))
	return answer
a = Reg_Polygon(100)