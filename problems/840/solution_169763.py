import math
def bolos(A, B, C):
    '''Calcula a quantidade máxima de bolos que João 
    consegue produzir dispondos de A xícaras de 
    farinha de trigo, B ovos e C colheres de sopa
    int, int, int -> int'''
    if A <2 or B<3 or C<5:
        return 0
    else:
        return min(math.floor(A/2),math.floor(B/3),
                   math.floor(C/5))