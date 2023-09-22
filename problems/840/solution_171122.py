from math import floor
def bolos(A,B,C):
    '''funcao que calcula bolo do jao'''
    return min(floor(A/2),floor(B/3),floor(C/5))