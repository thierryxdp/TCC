import math
def bolos(a,b,c):
    ''' Essa função determina a quantidade de xicaras de trigo(a), 
    ovos (b) e de colheres de sopa de leite (c), para fazer um bolo.'''
    return min (math.floor(a/2), math.floor(b/3), math.floor(c/5))