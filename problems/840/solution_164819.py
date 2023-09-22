import math 
def bolos(A,B,C):
    """ Calcula e retorna a quantidade máxima de bolos que João consegue fazer
    com os ingredientes que possui, xícaras de farinha - A, número de ovos-B,
    colheres de sopa de leite - C;
    int||float, int||float, int||float => int"""
    
    return math.floor(min(A/2,B/3,C/5))