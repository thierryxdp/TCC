def carros(pessoas,capacidade=5):
	"""fornce o número de carros necesárrios para transportar um determinado número de pessoas"""
	import math
    return math.ceil(pessoas/capacidade)