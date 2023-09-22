import math

def bolos(A,B,C):
    '''Função que calcula e retorna a quantidade máxima de bolos que
    pode ser feita com A xícaras de farinha de trigo, B ovos e C colheres
    de sopa de leite. A=float,B=int,C=float-> int'''
    return math.floor(min(A/2,B/3,C/5))