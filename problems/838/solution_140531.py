from math import ceil
def num_bombons (dinheiro, preço):
    """essa função calcula o maior número de bombons possível
	a ser comprado dados o dinheiro e o preço do item"""
    qtd_bombons = ceil(dinheiro/preço)