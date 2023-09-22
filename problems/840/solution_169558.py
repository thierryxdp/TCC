import math
def bolos (A, B, C):
    '''Calcula quantos bolos é possível fazer com os ingredientes disponíveis.
       int, int, int -> int'''
    a = math.floor (A / 2)
    b = math.floor (B / 3)
    c = math.floor (C / 5)
    return min(a, b, c)