import math
'''Definir quantos carros são necessarios para a viagem'''
'''int,int->int'''
def carros (pessoas, capacidade):
    return math.ceil(pessoas/capacidade)