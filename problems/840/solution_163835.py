def bolos(A,B,C):
    """Calcula quantos bolos é possível preparar com a quantidade de ingredientes disponível"""
    return min(A//2), min(B//3), min(C//5)