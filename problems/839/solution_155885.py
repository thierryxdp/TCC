def carros(num_pass,cap_carro=4):
	""""""
	Total=int(num_pass)/int(cap_carro)
	
	
	if num_pass>cap_carro:
		return int(Total)
    elif num_pass<cap_carro:
        return int(Total)+1
 
	elif cap_carro==0:
		return 0
	elif num_pass==0:
		return 0