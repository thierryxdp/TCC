import math
def carros(p,v=5):
	'''função para retornar o numero exato de carros necessarios para a viagem'''
    automoveis = math.ceil(p/v)
    return automoveis