import math
def bolos(A,B,C):
    """Função que calcula e retorna a maior quantidade possível de bolos, dados valores de A,B e C
    in,int,int> int"""
    return math.floor((A+B+C)/(2+3+5))