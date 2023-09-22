def bolos(A,B,C):
    quantidade_minimaA=A//2
    quantidade_minimaB=B//3
    quantidade_minimaC=C//5
    MinA=math.floor(quantidade_minimaA) 
    MinB=math.floor(quantidade_minimaB)
    MinC=math.floor(quantidade_minimaC)
    return min(MinA, MinB, MinC)