def carros(num_pass,cap_carro=4):
	""""""
	Total=(num_pass/cap_carro)

	if num_pass>cap_carro:
		return int(Total)
	elif Total!=int():
		return int(Total)+1
	elif cap_carro==0:
		return 0
	elif num_pass==0:
		return 0