import math
def bolos(A,B,C):
    """funçao que calcula a quantidade de bolos a ser 
    produzido a partir de uma quantidade de ingredientes A,B,C
    int,int,int->int"""
    return min(math.floor(A/2), math.floor(B/3), math.floor(C/5))