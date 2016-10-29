def read_input_count():
	inp_file = raw_input("Enter the input File Name: ")
	print inp_file
	
	with open(inp_file, "r") as inp:
		alpa_dict = {chr(k):0 for k in range(65,123)}
		for line in inp:
			for sub_line in line:
				if sub_line in alpa_dict:
					alpa_dict[sub_line] = int(alpa_dict[sub_line]) + 1

		for k,v in alpa_dict.iteritems():
			if v > 0:
				print "The number of times "+k+" appeared : "+str(v)

read_input_count()							