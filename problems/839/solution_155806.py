def carros(num_pass,cap_carro=4):
	""""""
	Total=(num_pass/cap_carro)
	if int(Total):
        return Total
	elif cap_carro==0:
		return 0
	elif num_pass==0:
		return 0
	elif float(Total):
		return Total+1