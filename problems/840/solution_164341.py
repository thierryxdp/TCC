def bolos(A,B,C):
    """calcula quantos bolos sao possiveis ser feitos com as quantidades: A xicaras de farinha, B ovos, C colheres de sopa de leite"""
    from math import *
    return min((floor(A/2)),(floor(B/3)),(floor(C/5)))