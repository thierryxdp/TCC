import math
def Bolos(a,b,c):
    """Calcular e retornar a quantidade de bolos possiveis de serem produzidos dado as quantidades de ingredientes a, b e c de entrada"""
        
    return math.floor(min(a/2, b/3, c/5))