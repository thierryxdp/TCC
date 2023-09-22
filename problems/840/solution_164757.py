import math
def bolos(A,B,C):
    '''calcular o numero maximo de bolos que joao consegue fazer com A xicaras de farinha de trigo,B ovos e C colheres de sopa de leite'''
    return int(min(A/2,B/3,C/5))