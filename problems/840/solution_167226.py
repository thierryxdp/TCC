from math import floor

def ingrediente_limitante(A,B,C):
    """Verifica qual é o ingrrediente limitante"""
return min(A/2,B/3,C/5)

def bolos(A,B,C):
    """Determina o quanto pode ser feito de bolo"""
    return floor(ingrediente_limitante)