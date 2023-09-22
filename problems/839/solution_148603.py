import math
def carros(pessoas,capacidade=5):
    '''Função que define a quantidade de carros necessários para transportar alguams pessoas'''
    ncarros = math.ceil(pessoas/capacidade)
    return ncarros