def carros(pessoas,lugares=5):
	"""funcao que retorna o numero de carros precisos a partir de uma quantidade de passageiros e lugares no carro"""
	if pessoas == 0:
		return 0
	elif pessoas < lugares or pessoas == lugares and pessoas != 0:
		return 1
	else: 
		pessoas%lugares !=0
		return (pessoas//lugares)+1