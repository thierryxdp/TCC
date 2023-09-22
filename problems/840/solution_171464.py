import math
def bolos(A,B,C):
    '''Dadas as quantidades de cada ingrediente, retorna a quantidade de bolos que João consegue fazer'''
    return max(math.floor(A/2),math.floor(B/3),math.floor(C/5))