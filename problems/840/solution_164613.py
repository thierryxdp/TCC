def bolos(A,B,C):
    """Calcula a quantidade de bolos a serem feitos com o numeros de ingredientes"""
    import math
    return max math.ceil(A//2,B//3,C//5)