import math
def carros(x,y=5):
    '''Dado x o número de pessoas e y a capacidade do veículo, retorna o número de veículos necessários'''
    return math.ceil(x/y)