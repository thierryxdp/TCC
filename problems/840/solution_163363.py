from math import *
def bolos(A, B, C): 
    """seguinto a receita de bolo: 2 xícaras A de farinha de trigo, 3 ovos, e
    5 colheres de sopa de leite. E considerando que serão feitas medidas exatas
    da receita, é calculado o número de bolos feitos"""
    return min(floor(A/2), floor(B/3), floor(C/5))