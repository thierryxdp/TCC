def bolos(A, B, C):
    """calcula quantos bolos podem ser feitos dados as quantidades de cada ingrediente A, B e C"""
    return min(A//2, B//3, C//5)