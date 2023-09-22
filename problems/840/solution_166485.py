import math
def bolos (A, B, C):
    """ Dividiremos os valores usando duas barras de divisão 
    para que nos retorne os menores valores inteiros.
    Usaremos F para farinha de trigo, O para ovos, L para leite e T para total"""
    F = A//2
    O = B//3
    L = C//5
    T = min(F, O, L)
    return T