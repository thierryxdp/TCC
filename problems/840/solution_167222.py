from math import floor

def bolos(A,B,C):
    """Calcula a quantidade máxima de bolos que podem ser
    feitos dados a quantidade de farinha(A), ovos(B) e
    leite(C)"""
    return min(floor(A/2,B/3,C/5))