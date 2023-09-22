import math
def bolos(A,B,C):
    """retorna o número de bolos que podem ser feitos com base na quantidade de ingredientes necessários/disponíveis de farinha de trigo A, ovos B e colheres de sopa de leite C
    int,int,int--->int"""
    return math.floor(min(A/2,B/3,C/5))