from math import *
def bolos(A,B,C):
    """calcula a quantidade maxima de bolos, dados o numero de xicaras de farinha de trigo A, o numero de ovos B e o numero de colheres de sopa de leite C"""
    return min(floor(A/2),floor(B/3),floor(C/5))