import math
def bolos (a, b, c):
    '''Calcule quantos bolos o joão consegue fazer, 
    a = número de xícaras de farinha de trigo;
    b = número de ovos;
    c = número de colheres;
    int, int -> int'''
    return math.min (a/2, b/3, c/5)