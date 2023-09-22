from math import*
def bolos (a,b,c):
    """Função que retorna a qtd de bolos que se pode fazer com os ingredientes disponíveis"""
    return min (a//2,b//3,c//5)