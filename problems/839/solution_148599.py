import math
def carros(pessoas):
    '''Função que define a quantidade de carros necessários para transportar alguams pessoas'''
    ncarros=math.ceil(pessoas)//5
    return ncarros