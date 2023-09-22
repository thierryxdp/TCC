import math
def bolos(A,B,C):
    '''Calcula a quantidade maxima de ingredientes dados ingredientes minimos
entrada: int, int, int, 
saida: int'''
    if ((C<5) and (B<3) and (A<2)):
        return math.ceil(A//2)
    return math.ceil(B//3)
    return math.ceil (C//5)