import math
def num_bombons(D,P):
"""Função que retorna o número máximo de bombons dado o dinheiro
disponível e o preço de cada bombom; float,float->int"""
	return math.ceil(D//P)