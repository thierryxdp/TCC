def bolos(A, B, C):
    """Calcula a quantidade máxima de bolos que João consegue fazer dados o número de xícaras de farinha de trigo (A), a quantidade de ovos (B) e a quantidade de colheres de sopa (C)
    entrada: int, int, int
    saída: int"""
    return min(A//2, B//3, C//5)