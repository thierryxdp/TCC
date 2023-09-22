import math
def carros(pessoas, capacidade = 5):
    '''Calcula o numero de carros necessarios dados a capacidade
    dos carros e o numero de passageiros'''
    	return math.ceil(pessoas/capacidade)