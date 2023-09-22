import math
def bolos(A,B,C):
    """Retorna a quantidade máxima de bolos que joão consegue fazer com os ingredientes disponíveis"""
    X=math.floor(A/2)
    O=math.floor(B/3)
    L=math.flor(C/5)
    return min(X,O,L)