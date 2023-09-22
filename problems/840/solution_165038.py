import math
def bolos(A, B, C):
    '''Função que retorna a quantidade máxima de bolos que joão consegue
    fazer dadas as quantidades A, B, C e as quantidades da receita do bolo
    int, int, int -> int'''
    
    return min(int(A/2), int(B/3), int(C/5))