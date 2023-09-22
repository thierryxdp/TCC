import math
def bolos(A,B,C):
    '''Função que determina a quantidade máxima de bolos que é
    possível fazer, dadas as quantidades de xícaras, ovos e
    colheres de sopa de leite; int,int,int->int'''
    x=math.ceil(A/2)
    x=math.ceil(B/3)
    x=math.ceil(C/5)
    return min(A/2,B/3,C/5)