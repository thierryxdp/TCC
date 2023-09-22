import math

def bolos(a,b,c):
    '''Essa função determina a quantidade máxima
    de bolos inteiros que se consegue fazer'''
    if (a<2,b<3,c<5):
        return 0
    else:
        return math.floor((a+b+c)/(2+3+5))