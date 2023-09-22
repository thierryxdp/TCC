import math
def bolos(A,B,C):
    """ Função que retorna a quantidade de bolos que é
    possível dados os ingredientes """
    return math.ceil(min(A//2,B//3,C//5))