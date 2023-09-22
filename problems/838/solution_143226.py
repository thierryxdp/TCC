import math
def num_bombons(dinheiro,preco):
    '''
    calcula e retorna a quantidade de bombons que o dinheiro que tem consegue comprar dado o preço de um bombom;
    float, float -> int
    ''''
	return math.floor(dinheiro/preco)