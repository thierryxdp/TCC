from math import *

def ingredientes(a,b,c):
    '''função que calcula a quantidade de bolos produzidos pelo tanto de ingredientes disponíveis; int, int, int -> int'''
    return (a/2),(b/3),(c/5)
def bolos(a,b,c):
    '''função que retrata o mínimo de bolos produzidos; float, float, float -> int'''
    return min(floor(ingredientes(a,b,c)))