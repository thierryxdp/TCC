def carros(pessoas,capacidade=5):
	"""fornce o número de carros necesárrios para transportar um determinado número de pessoas"""
	return math.ceil(pessoas/capacidade)