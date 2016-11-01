__author__ = 'jiths'
'''Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.'''

def calculator():
    inp1 = raw_input("Enter first input\n")
    inp2 = raw_input("Enter second input\n")

    op = raw_input("Enter Operator\n")

    if op == "+":
    	print inp1+"+"+inp2+"="
    	print int(inp1) + int(inp2)
    elif op == "-":
    	print inp1+"-"+inp2+"="
    	print int(inp1) - int(inp2)

    elif op == "*":
    	print inp1+"*"+inp2+"="
    	print int(inp1) * int(inp2)   	
    else:
    	print "Invalid Entry"	

calculator()    	