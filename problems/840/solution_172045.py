import math
def bolos ( a, b, c):
    '''Calcula a quantidade máxima de bolos que João consegue fazer.
    Dados os ingredientes a, b e c.'''
    return math.floor(min(a/2 + b/3 + c/5))