def bolos(A,B,C):
    """Calcula  a quantidade maxima de bolos que João consegue fazer 
    dado valores para A, B e C"""
    import math
    return min((math.floor(A/2)),(math.floor(B/3)),(math.floor(C/5)))