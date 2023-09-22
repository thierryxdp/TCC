import math
def bolos(A,B,C):
    """retorna a quantidade de bolo que dá pra fazer com os ingredientes A,B,C
    float,float->float"""
    return min(math.floor(A/2),math.floor(B/3),math.floor(C/5))