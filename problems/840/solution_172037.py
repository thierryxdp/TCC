import math
def bolos ( a, b, c):
    '''Calcula a quantidade máxima de bolos que João consegue fazer.
    Dados os ingredientes a, b e c.'''
    return math.floor(((a/2) + (b/3) + (c/5)))//3