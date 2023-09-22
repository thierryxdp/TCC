def bolos(A, B, C):
    """Função que determina qual a quantidade maxima de bolos
    que ele consegue fazer
    int, int, int -> int"""
    
    return min(A//2, B//3, C//5)