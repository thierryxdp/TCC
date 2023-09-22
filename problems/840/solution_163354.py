from math import floor

def bolos(A,B,C):
    '''Calcula e retorna a quantidade de bolos que João conseguirá fazer usando os
    ingredientes que tem em casa dados A = xícaras de farinha de trigo, B = ovos
    e C = colheres de sopa de leite.
    Só aceita valores positivos para A, B e C
    int, int, int -> int'''
    return min(floor(A/2),floor(B/3),floor(C/5))