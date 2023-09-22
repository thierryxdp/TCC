import math
def bolos (A,B,C):
    '''retorna o numero de bolos que joao fara
    int/float,int,int/float'''
    return min(math.floor(A/2),math.floor(B/3),math.floor(C/5))