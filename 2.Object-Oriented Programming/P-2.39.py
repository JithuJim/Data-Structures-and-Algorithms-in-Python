
from abc import abstractmethod
import math

class Polygon:
	def __init__(self):
		pass

	@abstractmethod	
	def area(self):
		'''return area'''

	@abstractmethod
	def perimeter(self):
		'''return perimeter'''		

class Triangle(Polygon):
	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c

	def area(self):
		s = (self.a+self.b+self.c)/2
		s1 = s*(s-self.a)*(s-self.b)*(s-self.c)
		return math.sqrt(s1)

	def perimeter(self):
		return self.a+self.b+self.c

class IsoscelesTriangle(Triangle):
	def __init__(self,a,b,c):
		Triangle.__init__(self,a,b,c)


class Quadrilateral(Polygon):
	def __init__(self,a,b,c,d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d

	def area(self):
		return (self.a+self.b+self.c+self.d)/2

	def perimeter(self):
		return self.a+self.b+self.c	+self.d	

class CreatePolygon(Triangle,Quadrilateral):
	def __init__(self,type='',a=0,b=0,c=0,d=0):
		Triangle.__init__(self,a,b,c)
		Quadrilateral.__init__(self,a,b,c,d)
		self.type = type

	def accept_polygon(self):
		self.type = raw_input("Enter the type of polygon you would like to create\n")
		self.a = int(raw_input("Enter first side\n"))
		self.b = int(raw_input("Enter second side\n"))
		self.c = int(raw_input("Enter third side\n"))

		if self.type == "Quadrilateral":
			self.d = int(raw_input("Enter fourth side\n"))

	def poly_area(self):
		if self.type == "Quadrilateral":
			return Quadrilateral(self.a,self.b,self.c,self.d).area()
		else:
			return Triangle(self.a,self.b,self.c).area()	

	def poly_peri(self):
		if self.type == "Quadrilateral":
			return Quadrilateral(self.a,self.b,self.c,self.d).perimeter()
		else:
			return Triangle(self.a,self.b,self.c).perimeter()				
			

t = Triangle(3,4,5)
print t.area()
print t.perimeter()		

i = IsoscelesTriangle(6,6,10)	
print i.area()
print i.perimeter()

c = CreatePolygon()
c.accept_polygon()
print c.poly_area()
print c.poly_peri()


			
