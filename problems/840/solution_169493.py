import math
def bolos(A,B,C):
    '''Calcula a quantidade máxima de bolos que João consegue
    produzir, dado que ele possui A xícaras de farinha, B ovos
    C colheres de sopa.
    int, int, int -> int'''
    return math.floor(A+B+C)/10