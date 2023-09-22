import math
def bolos(A,B,C):
    """calcula o numero maximo de bolos que podem ser feitos dados os ingrediente, xicaras
    de farinha(A), ovos(B) e colheres de leite(C)"""
    a = math.floor(A/2)
    b = math.floor(B/3)
    c = math.floor(C/5)
    return min(a,b,c)