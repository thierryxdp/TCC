import math
def carros(pessoas,capacidade=5):
	'função que retorna quantidade de carros para pessoas.int, int=>int'
   	automóveis = math.ceil(pessoas / capacidade)
	return automóveis