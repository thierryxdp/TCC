from math import floor
def bolos(a,b,c):
    '''calcular quantidade de bolos possiveis a partir dos ingredientes disponíveis'''
    return math.floor(min(a/2,b/3,c/5))