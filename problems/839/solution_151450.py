import math
def carros(p,v=5):
    '''calcular quantos carros sao necessarios numa viagem'''
    '''int, int -> int'''
    return math.ceil (p//v)