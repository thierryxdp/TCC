import math
def bolos(a,b,c):
    """calcula e retorna a quantidade de bolos que joao consiguira fazer"""
    return math.min(a//2,b//3,c//5)