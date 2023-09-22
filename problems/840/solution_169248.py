import math
def bolos(A, B, C):
    ''' calcule a quantidadem máxima de bolos. 
    dado os ingredientes A=2, B=3, C=5 '''
    qtd_A = A//2
    qtd_B = B//3
    qtd_C = C//5
    return min(qtd_A, qtd_B, qtd_C)