import math
def carros (p,c=5):
    """cálculo do número exato de veículos c necessários para transportar um determinado número de pessoas p:
    int, int -> int"""
    return math.ceil(p/c)