import math
def bolos(A,B,C):
    """Função que determina a quantidade máxima de bolos
    que podem ser feitos a partir dos ingredientes A,B e C
    dados como entrada, int, int -> int"""
    return math.floor((min(A/2,B/3,C/5)))