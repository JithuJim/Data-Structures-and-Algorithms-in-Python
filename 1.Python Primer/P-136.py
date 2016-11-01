'''Write a Python program that inputs a list of words, separated by whitespace,
and outputs how many times each word appears in the list. You
need not worry about efficiency at this point, however, as this topic is
something that will be addressed later in this book.'''
from collections import Counter
def input_words():
	list__ = raw_input("Input the list of words\n")

	list__ = list__.split()
	l=Counter(list__)
	print l

input_words()		