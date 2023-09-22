def bolos(A,B,C):
    """calcula a quantidade maxima de bolos
    int,int,int->int"""
    farinha = A//2
    ovos = B//3
    leite = C//5
    return min(farinha,ovos,leite)