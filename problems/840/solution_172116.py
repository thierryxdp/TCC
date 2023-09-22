import math 
def bolos (a, b, c):
    '''Calcular a quantidade máxima de bolos 
    que podem ser produzidos com os ingredientes
    a, b e c disponíveis'''
    return min(math.floor(a/2), math.floor(b/3), math.floor(c/5))