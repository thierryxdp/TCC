import math
def bolos(A, B, C):
    farinha = A//2
    ovos = B//3
    leite = C//5
    return math.min(farinha, ovos, leite)