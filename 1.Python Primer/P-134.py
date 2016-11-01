'''A common punishment for school children is to write out a sentence multiple
times. Write a Python stand-alone program that will write out the
following sentence one hundred times: I will never spam my friends
again. Your program should number each of the sentences and it should
make eight different random-looking typos.'''

def punishment_program():
	for ele in range(1,24):
		for i in range(0,3):
			print str(ele)+'.'+'I will never spam my friends again.'


punishment_program()			