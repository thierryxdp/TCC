import math
def carros(pessoas,capacidade=5):

	'''(int, int=>int) calcula a quantidade de carros neccessario para ir na viagem'''

	automovel = math.ceil(pessoas / capacidade)
	return altomovel