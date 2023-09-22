def carros(x, y=5):
	'''calcula a quantidade de carros necessária para determindada viagem, dadas a quantidade de pessoas e a capacidade dos carros (que será considerada 5, caso nenhum valor seja informado.'''
    return math.ceil(x/y)