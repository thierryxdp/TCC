#questão 3 bolos
def xicaras(A):
    return int(A)//2

def ovos(B):
    return int(B)//3

def colheres(C):
    return int(C)//5

def bolos(A,B,C):
    return min(xicaras(A),ovos(B),colheres(C))