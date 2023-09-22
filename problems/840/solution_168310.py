def bolos (A,B,C):
    """calcula a quantidade maxima de bolos que poderao ser feitos,
    dados as quantidades de A, B e C disponiveis dos
    ingredientes necessários"""
    return min(A//2, B//3, C//5)