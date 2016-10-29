
def convert_polynomial(poly):
	#x**2 + 2*x + 1

	split_poly = str(poly).split('+')
	first_deriv  = ''
	for ele in split_poly:
		if 'x' in ele: 
			if ele[0].isdigit():
				mul_1 = int(ele[0])
			else:
				mul_1 = 1
				
			if ele[-1].isdigit():
				mul_2 = int(ele[-1])
				new_degree = mul_2 - 1
			else:
				mul_2 = 1
				new_degree = 0	
				
			first_deriv += str(mul_1*mul_2)+'x^'+ str(new_degree)+'+'
			
	if 'x^0' in first_deriv:
		first_deriv = first_deriv.replace('x^0','')	
	first_deriv = first_deriv.rstrip('+')
	return first_deriv

print convert_polynomial("2x^2+6x+1")			
				