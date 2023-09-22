from math import *
def carros(pessoas,capacidade):
    '''
Função que receba comno entrada o número de pessoas que irão
na viagem e a capacidade dos veículos, e retorne a quantidade
de veículos necessários.
	'''
    if capacidade == '':
        return ceil(pessoas/5)
    else:
    	return ceil(pessoas/capacidade)