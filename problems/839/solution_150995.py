import math
def carros(P, C=5):
    '''função que retorna o número de carros de capacidade C necessários para transportar P pessoas
    int -> int'''
    return math.ceil(P/C)