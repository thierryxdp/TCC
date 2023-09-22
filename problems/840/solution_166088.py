import math
def bolos(A,B,C):
    '''Retorna a quantidade de bolos que é possível
    fazer dado A xicaras de farinha, B ovos e C colheres
    de sopa de leite; int,int,int -> int'''
    return min(A/2,B/3,C/5)