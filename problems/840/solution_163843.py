def bolos(A,B,C):
    """Calcula a quantidade de bolos que é possível preparar com os ingredientes disponíveis"""
    farinha = A//2
    ovos = B//3
    leite = C//5
    return min(farinha,ovos,leite)