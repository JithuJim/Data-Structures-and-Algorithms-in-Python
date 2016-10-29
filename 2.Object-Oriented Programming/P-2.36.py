import random
from random import randint
import threading

class Bear:
	def __init__(self):
		pass

class Fish:
	def __init__(self):
		pass 

class Ecosystem:
	def __init__(self):
		self.river = []
		self.count = 0

	def create_element(self):
		for ele in random.sample(range(100), 10):
			if ele > 15:
				if ele % 2 == 0:
					self.river.append(Bear())
				else:
					self.river.append(Fish())
			else:
				self.river.append(None)			

	def moving_around(self):
		t = threading.Timer(1,self.moving_around)
		current_index = (randint(0,len(self.river)-1))
		new_index = (randint(0,len(self.river)-1))

		if isinstance(self.river[current_index],Fish) and isinstance(self.river[new_index],Fish):
			print self.river
			empty_set = self.river.index(next(obj for obj in self.river if obj==None))
			print str(empty_set)+ "empty set fish"
			if not empty_set:
				self.river.append(Fish())
			else:
				self.river[empty_set] = Fish()
		elif isinstance(self.river[current_index],Bear) and isinstance(self.river[new_index],Bear):	
			print self.river
			empty_set = self.river.index(next(obj for obj in self.river if obj==None))
			print str(empty_set) + "empty set bear"
			if not empty_set:
				self.river.append(Bear())
			else:
				self.river[empty_set] = Bear()
		elif self.river[current_index] == None or self.river[new_index] == None:
			pass
			print "One is None"		
		else:
			if isinstance(self.river[current_index],Fish):
				self.river[current_index] = None
			else:
				self.river[new_index] = None		
		t.start()
		self.count += 1
		if self.count == 1:
			t.cancel()
	
		print current_index
		print new_index
		print isinstance(self.river[current_index],Bear) 		
		print isinstance(self.river[current_index],Fish) 	
		print isinstance(self.river[new_index],Bear) 	
		print isinstance(self.river[new_index],Fish) 	
		print self.river
		
e = Ecosystem()
e.create_element()	
e.moving_around()					

