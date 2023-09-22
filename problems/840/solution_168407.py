import math
def bolos(A,B,C):
    '''retorna a quantidade máxima de bolos
    possível de fazer, dados a quantidade de xícara
    de farinha A, de ovos B, e de colheres de sopa
    de leite C.
    int, int, int -> int'''
    return min(A//2, B//3, C//5)