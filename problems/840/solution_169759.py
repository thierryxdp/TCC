import math
def bolos(A, B, C):
    '''Calcula a quantidade máxima de bolos que João 
    consegue produzir dispondos de A xícaras de 
    farinha de trigo, B ovos e C colheres de sopa
    int, int, int -> int'''
    if A <=2 or B<=3 or C<=5:
        return 0
    else:
        return math.floor((A/2+B/3+C/5)/3)