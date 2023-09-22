import math

def bolos(A,B,C):
    '''funcao que calcula a quantidade maxima de bolos
    que joao consegue fazer com a quantidade de in
    '''
    return min(A//2, B//3, C//5)