import math
def bolos(A,B,C):
    """Calcula e retorna o número de bolos que podem ser feitos com os ingredientes A,B e C"""
    return math.floor(min(math.floor(A/2),math.floor(B/3), math.floor(C/5)))