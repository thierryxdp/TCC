from math import *

def bolos(a,b,c):
    '''função que calcula a quantidade de bolos produzidos pelo tanto de ingredientes disponíveis; int, int, int -> int'''
    return min(from((a/2),(b/3),(c/5)))