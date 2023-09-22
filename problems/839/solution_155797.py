def carros(num_pass,cap_carro=4):
	""""""
	
	if num_pass>4:
		return int(num_pass/cap_carro)
	elif num_pass<4:
		return float((num_pass/cap_carro)**0)