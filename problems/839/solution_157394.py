import math
def carros (pessoas,capacidade=4):
	'''calcula quantos carros são necessários para levar uma determinada quantidade de pessoas numa viagem'''
    resultado= pessoas//capacidade
    return math ceil (resultado)