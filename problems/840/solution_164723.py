import math
from math import floor
def bolos(a,b,c):
    '''Calcula e retorna a quantidade maxima de bolos feitos dado os valores de a,b e c'''
    return floor(((a//2)+(b//3)+(c//5))//3)