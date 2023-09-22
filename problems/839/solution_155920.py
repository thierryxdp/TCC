def carros(num_pass,cap_carro=5):

	""""""	
    Total=(num_pass/cap_carro)
    qnt_carros = (math.ceil(Total/cap_carro))


	if num_pass>cap_carro:

		return int(Total)

	elif cap_carro==0:

		return 0

	elif num_pass==0:

		return 0