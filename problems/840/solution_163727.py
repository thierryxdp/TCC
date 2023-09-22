def bolos(A,B,C):
    """calcula e retorna a quantidade máxima inteira de bolos que é possível fazer dados os ingredientes A,B e C"""
    return min(A//2,B//3,C//5)