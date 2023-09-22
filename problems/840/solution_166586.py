from math import*
def bolos(A,B,C):
    '''calcular a quantidade de bolos que João consegue fazer com A xicaras de farinha de trigo,B ovos e C colheres de sopa de leite'''
    return round(min((A/2), (B/3), (C/5)))