def bolos(A,B,C):
    """fnção que retorna a maior quantidade de bolos possiveis de serem feitos a partir dos ingredientes"""
    return min(A//2, B//3,C//5)