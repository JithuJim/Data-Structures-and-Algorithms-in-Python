class EbookReader:
	
	def __init__(self):
		self.books = ["The Arabian Nights","Grimm's Fairy Stories","The Jungle Book","My Antonia","Mary Poppins Comes Back"]
		self.purchased_books = []

	def buy_books(self):
		for ele in self.books:
			print ele
		input = raw_input("Select the book to buy")	

		self.purchased_books.append(input)

	def view_purchased_books(self):
		for ele in self.purchased_books:
			print ele

	def read_purchased_books(self):
		inp_file = raw_input("Enter the input File Name: ")
		with open(inp_file, "r") as inp:
			for line in inp:
				print line 



e = EbookReader()
e.buy_books()
e.view_purchased_books()
e.read_purchased_books()							
