def carros(pessoas,capacidade=5):
	"""Função que calcula a quantidade de carros para levar as pessoas"""
	import math
    return math.ceil(pessoas/capacidade)