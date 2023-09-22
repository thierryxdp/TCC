import math

def carros(p, c = 5):
    '''Retorna o número de carros necessários para que caiba todas as pessoas dentro.
    int, int -> int'''
    return math.ceil(p / c)