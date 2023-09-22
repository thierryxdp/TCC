from math import ceil
def carros (pessoas,capacidade)
	'''
    funcao para calcular numero de carros necessarios
    para transportar um numero especifico de pessoas
    dado o numero de pessoas e capacidade do carro
	(int,int)->int
    '''
    return int(ceil(pessoas/capacidade))