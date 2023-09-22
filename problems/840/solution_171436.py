def bolos(A,B,C):
    '''retorna a quantidade maxima de bolos que joao consegue fazer
    sendo A=xicaras de farinhas; B=ovos;C=colheres de sopa'''
    import math
    return math.floor(min(A/2,B/3,C/5))