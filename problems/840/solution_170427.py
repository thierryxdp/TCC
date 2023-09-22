import math
def xicara(A):
    '''quantas xicaras de farinha precisam'''
    return a//2
def ovos(B):
    ''' quantos ovos precisam '''
    return b//3
def leite(C):
    '''quanto de leite precisa''' 
    return c//5
def bolos(A,B,C):
    """quantida de bolos possiveis"""
    return min(xicara(A),ovos(B),leite(C))