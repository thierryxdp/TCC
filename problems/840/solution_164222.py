import math
def bolos(a,b,c):
    """Função que calcula a quantidade de ingedites a,b,c de entrada e da a quantidade de bolos possiveis de produzir"""
        
    return math.floor(min(a/2, b/3, c/5))