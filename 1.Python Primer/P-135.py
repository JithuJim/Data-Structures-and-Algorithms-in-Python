'''The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20, . . . ,100.'''

from random import randint
from itertools import groupby

def test_birthday(n):
	random_birthdays = [randint(1,31) for ele in range(n)]
	frequency_ = [len(list(group)) for key, group in groupby(random_birthdays)]
	count = 0
	for ele in frequency_:
		if ele > 1:
			count += 1
	return "Two people in a room have same birthday"	if count > 0 else "Two people in a room do not have same birthday"

print "5 people group -->"+ str(test_birthday(5))
print "10 people group -->"+ str(test_birthday(10))
print "15 people group -->"+ str(test_birthday(15))
print "20 people group -->"+ str(test_birthday(20))
print "25 people group -->"+ str(test_birthday(25))
print "30 people group -->"+ str(test_birthday(30))
print "35 people group -->"+ str(test_birthday(35))
print "40 people group -->"+ str(test_birthday(40))
print "45 people group -->"+ str(test_birthday(45))
print "50 people group -->"+ str(test_birthday(50))