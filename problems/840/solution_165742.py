from math import *
def bolos(A,B,C):
    '''calcular a quantidade maxima de bolos que se é possivel fazer'''
    '''int,int,int -> int'''
    return min(A//2,B//3,C//5)