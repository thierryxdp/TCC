def bolos(A,B,C):
    """Função que calcula a quantidades de bolos feita dado a quantidade de ingredientes.
       float, float, float -> float"""
    return min(A//2, B//3, C//5)