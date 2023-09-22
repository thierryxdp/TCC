import math
def bolos(A,B,C):
    """ retorna a quantidade maxima de bolos que joao consegue fazer"""
    return math.floor(A//2+B//3+C//5)