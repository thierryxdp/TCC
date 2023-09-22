from math import *

def ingredientes(a,b,c):
    '''função que calcula a quantidade de bolos produzidos pelo tanto de ingredientes disponíveis; int, int, int -> int'''
    return (a//2),(b//3),(c//5)
    
def bolos(a,b,c):
    '''função que da o número mínimo de bolos produzidos'''
    return min(ingredientes(a,b,c))