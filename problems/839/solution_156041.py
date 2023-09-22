from math import *
def carros(pessoas,capacidade=5):
    '''
Função que receba comno entrada o número de pessoas que irão
na viagem e a capacidade dos veículos, e retorne a quantidade
de veículos necessários.
	'''
    return ceil(pessoas/capacidade)