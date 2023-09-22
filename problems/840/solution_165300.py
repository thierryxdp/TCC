from math import *
def bolos(A,B,C):
    '''determina a quantodade máxima de bolos que João consegue fazer com A xícaras de trigo, B ovos e C colheres de leite'''
   return min(floor(A/2),floor(B/3),floor(C/5))