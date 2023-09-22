import math

def bolos(a,b,c):
    """retorna o numero maximo de bolos que se pode fazer a partir das xicaras de farinha a, dos ovos b e das coleres de leite c
       int, int, int-> int"""
    return max(2//a,3//b,5//c)