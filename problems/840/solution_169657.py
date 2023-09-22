import math

def bolos(A,B,C):
    '''funcao que calcula a quantidade maxima de bolos
    que joao consegue fazer com a quantidade de 
    ingredientes disponiveis
    :param A: int
    :param B: int
    :param C: int
    :return: int
    '''
    return min(A//2, B//3, C//5)