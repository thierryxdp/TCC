def bolos (a, b, c):
    '''retorna o numero de bolos que da pra fazer com os ingredientes
    int/float, int, int/float -> int'''
    import math
    return min (math.floor(a/2), math.floor(b/3), math.floor(c/5))