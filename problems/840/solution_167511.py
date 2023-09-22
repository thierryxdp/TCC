import math
def bolos (a,b,c):
    ''' calcula e retorna o valor máximo de bolos que joão 
    consegue fazer com dados as quantidades de a, b e c'''
    return min(a//2,b//3,c//5)