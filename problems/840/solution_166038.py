from math import*
def bolos(A,B,C):
    """Calcula a quantidade maxima de bolos que pode ser feita dado uma certa quantidade de ingredientes disponiveis"""
    return min(A//2,B//3,C//5)