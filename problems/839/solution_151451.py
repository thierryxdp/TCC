import math
def carros(p,v=5):
    '''calcular quantos carros sao necessarios numa viagem'''
    return math.ceil (p//v)