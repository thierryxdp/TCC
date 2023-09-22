from math import ceil
def num_bombons(dinheiro, preço):
    """essa função calcula o maior número de bombons
	 a serem comprados dados o dinheiro e o preço do item"""
    qtd_bombons = math.ceil*(dinheiro/preço)
    return qtd_bombons