import math

def carros(p,c=5):
	'''Retorna o número mínimo de carros necessários para a viagem dado o número 
    de pessoas. Caso a capacidade dos veículos não sejam informadas, será 
    considerada a capacidade convencional de 5 pessoas; int, int-> int'''
	return math.ceiling(p/c)