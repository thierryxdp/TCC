from math import *
def bolos(A,B,C):
    '''determina a quantodade máxima de bolos que João consegue fazer com A xícaras de trigo, B ovos e C colheres de leite'''
    return min(roound(A/2),round(B/3),round(C/5))