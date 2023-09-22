from math import floor

def bolos(A,B,C):
    """Determina o quanto pode ser feito de bolo"""
return min(floor(A/2),floor(B/3),floor(C/5))