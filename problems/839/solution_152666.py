import math

def carros(P,C):
    '''Dados o numero de pessoas(P)e a capacidade (C),retorna o numero de carros necessarios'''
    return math.ceil(P/C)