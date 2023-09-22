import math

def num_bombons(dinheiro, preco):
	'''funcao que define o maior numero de bombons que 
    Pedro podera comprar de acordo com seu dinheiro.
    :param dinheiro: float
    :param preco: float
    :param return: int
    '''
    return math.floor(dinheiro/preco)