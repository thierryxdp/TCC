import math

def bolos(A,B,C):
    '''função que calcula o número máximo de bolos que João consegue fazer
    com os ingredientes que tem disponível, seguindo a receita. João dispõe
    de A xícaras de farinha de trigo, B ovos e C colheres de sopa de leite
    int, int, int -> int'''
    return math.floor(min(A/2,B/3,C/5))