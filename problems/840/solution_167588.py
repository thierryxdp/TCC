def bolos(A,B,C):
    """calula e retorna a quantidade máxima de bolos que João consegue
    fazer,dados as quantidades dos ingredientes necessárias"""
    return max((A//2)+(B//3)+(C//5))