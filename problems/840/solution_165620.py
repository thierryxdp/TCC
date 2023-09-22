import math
def bolos(A, B, C):
    '''Informa a quantidade mínima possível de bolos com os ingredientes que a pessoa possui.
       int, int, int -> float'''
    return min(round((A/2)-0.4999999, 0), round((B/3)-0.49999999, 0), round((C/5)-0.49999999, 0))