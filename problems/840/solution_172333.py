def bolos(A, B, C):
    """funcao que calcula o numero de bolos que joao consegue fazer dados os ingredientes que tem em casa"""
    return min(A//2, B//3, C//5)