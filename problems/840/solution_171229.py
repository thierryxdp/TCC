import math
def bolos(A,B,C):
    """funcao que define a quantidade de bolos possiveis de fazer com a quantidade de ingredientes"""
    n1 = A//2
    n2 = B//3
    n3 = C//5
    return min(n1,n2,n2)