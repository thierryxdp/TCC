import math
from math import floor
def bolos(a,b,c):
    '''Calcula e retorna a quantidade maxima de bolos feitos dado os valores de a,b e c'''
    a=2 or a>2
    b=3 or b>3
    c=5 or b>5
    return floor(([a//2]+[b//3]+[c//5])//3)