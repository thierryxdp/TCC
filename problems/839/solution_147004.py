import math

def carros(pessoas, capacidade=5):
	''' Define quantos veículos de capacidade 'capacidade' são necessários para carregar 'pessoas' pessoas '''
	return math.ceil(pessoas/capacidade)