def bolos(A,B,C):
    """Recebe os valores A,B e C, calcula com as quantidades necessárias do bolo e retorna a quantidade de bolos"""
    import math
    F = A/2
    O = B/3
    L = C/5
    math.floor(F,O,L)
    b = min(F,O,L)
    return b