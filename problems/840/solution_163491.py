import math
def bolos(a,b,c):
    '''Essa função determina a quantidade máxima
    de bolos inteiros que se consegue fazer'''
    return math.floor((a+b+c)/(2+3+5))
if a<2 return 0
if b<3 return 0
if c<5 return 0