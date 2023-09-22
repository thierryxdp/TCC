import math
def carros(pessoas,capacidade_veiculo=5):
	'''
calcula e retorna a quantidade de carros necessarios
para transportar certa quantidade de pessoas dados
a quantidade de pessoas e a capacidade do veiculo
como entrada
	'''
    return math.ceil(pessoas/capacidade_veiculo)