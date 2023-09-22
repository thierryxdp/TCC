import math
def bolos(a,b,c):
    """função que determina a quantidade maxima de bolos
    que João consegue fazer
    int,int,int -> int"""
    return math.floor(min(a/2,b/3,c/5))