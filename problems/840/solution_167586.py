from math import *
def bolos(A, B, C):
    '''funçao determina a quantidade de bolos possiveis de serem feitos com a quantidade de ingredientes'''
    return floor(min(A/2, B/3, C/5))