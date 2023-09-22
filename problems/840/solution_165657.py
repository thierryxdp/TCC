from math import *
def bolos(A,B,C):
    """funcao que calcula a quantidade bolos a serem feitas,
       dada a quantidade de xicaras de farinhas (A), ovos (B)
       e colheres de leite (C) de entrada
       int, int, int -> int """
    x = A//2
    y = B//3
    z = C//5
    return min(x,y,z)