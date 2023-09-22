import.math

def carros(pessoas,capacidade=5)
	'''Calcula quantos carros são necessários para transportar determinada quantidade de pessoas'''
	automoveis= (pessoas/capacidade)
    return math.ceil automoveis