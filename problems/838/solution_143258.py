import math
def num_bombons(dinheiro,preco):
    """Retorna o número de bombons que se pode comprar com os valores dados de dinheiro e preço do bombom."""
	return math.floor(dinheiro/preco)