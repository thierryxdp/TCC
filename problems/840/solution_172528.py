import math
def bolos (A,B,C):
    quantidade_mínimaA=A//2
    quantidade_mínimaB=B//3
    quantidade_mínimaC=C//5
    MinA=math.floor (quantidade_minimaA)
    MinB=math.floor (quantidade_minimaB)
    MinC=math.floor (quantidade_minimaC)
    return min(MinA, MinB, MinC)