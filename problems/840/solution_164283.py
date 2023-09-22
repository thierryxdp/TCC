from math import *
def bolos(A,B,C):
    """Calcula e retorna a quantidade maxima de bolos que Joao consegue
    fazer, sendo A = xicaras de farinha, B = ovos e C = colheres 
    de sopa de leite"""
    A = floor(A/2)
    B = floor(B/3)
    C = floor(C/5)
    return min(A,B,C)