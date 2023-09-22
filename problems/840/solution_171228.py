import math
def bolos(A,B,C):
    """funcao que define a quantidade de bolos possiveis de fazer com a quantidade de ingredientes"""
    n1 = math.ceil((A//2)-0.5)
    n2 = math.ceil((B//3)-0.5)
    n3 = math.ceil((C//5)-0.5)
    return min(n1,n2,n2)