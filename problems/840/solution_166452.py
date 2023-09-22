from math import *
def bolos(A,B,C):
    """retorna o maior número de bolos que João pode fazer com A xícaras de farinha, B ovos e C colheres de sopa de leite; int, int, itn -> int"""
    return min(A//2,B//3,C//5)