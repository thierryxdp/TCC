import math
def bolos(a,b,c):
    """calcula a quantidade maxima de bolos a serem feitos dada a quantidade de farinha de trigo(a), ovos(b) e leite(c)"""
    return min(a//2,b//3,c//5)