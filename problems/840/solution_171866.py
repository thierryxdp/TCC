import math
def bolos(A,B,C):
    '''retorna a quantidade máxima de bolos que se consegue fazer com A xícaras de farinha de trigo, B ovos e C colheres de sopa de leite'''
    '''int,int,int->int'''
    return min(math.floor(A/2),math.floor(B/3),math.floor(C/5))