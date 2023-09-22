import math
def bolos(A,B,C):
    """Calcula e retorna o número de bolos que podem ser feitos com os ingredientes A,B e C"""
    return math.floor(((A/2)+(B/3)+(C/5))/3)