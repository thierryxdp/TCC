from math import *
def bolos(A,B,C):
    '''Calcula a quantidade maxima de bolos que conseguem ser feitos dados os valores de entrada a quantidade de cada ingrediente'''
    ''' int,int,int ->int'''

    return min(A//2,B//3,C//5)