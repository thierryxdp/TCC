def bolos(A,B,C):
    """calula e retorna a quantidade máxima de bolos que João consegue
    fazer,dados as quantidades dos ingredientes necessárias"""
    import math
    return min(A/2,B/3,C/3)