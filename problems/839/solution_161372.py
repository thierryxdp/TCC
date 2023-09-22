import math
def carros(pessoas,capacidade=5):
    '''funcao que calcula e retorna o numero de carros necessarios para uma viajaem'''
    return math.ceil (pessoas/capacidade)