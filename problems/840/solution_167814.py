import math
def bolos (A,B,C):
    """função que calcula o número de bolos com trigo, ovo e leite"""
    return math.max(A//2,B//3,C//5)