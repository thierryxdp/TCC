import math as m

def carros (pessoas,carros=5):
    '''
    	Funcao que calcula quantos veiculos sao necessarios para
        transportar uma quantidade de pessoas, dados o numero de
        pessoas e, caso o veiculo possua capacidade diferente de 5,
        informar a capacidade do veiculo (quantas pessoas o veiculo
        pode transportar).
	'''
    return m.ceil(pessoas/carros)