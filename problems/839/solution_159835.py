import math
def carros(pessoas,capacidade=5):
    '''Calcula a quantidade de veículos necessários para transportar
    um grupo de pessoas em uma viagem'''
    return math.ceil(pessoas/capacidade)