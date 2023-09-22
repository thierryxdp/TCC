import math

def bolos(A,B,C):
    '''Dados (A,B,C), retorna o numero maximo de bolos possiveis'''
    return math.floor(min(A/2,B/3,C/5))