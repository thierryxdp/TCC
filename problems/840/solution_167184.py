import math
def bolos(A,B,C):
    """função que calcula e retorna a maior quantidade de bolos possível dadosvalores dos ingredientes A,B e C
    in,int,int> int"""
    return math.floor(min(A/2,B/3,C/5))