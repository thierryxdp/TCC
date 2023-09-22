def bolos(A,B,C):
    """Calcula quantos bolos pode-se fazer com os ingredientes disponiveis"""
    a = A//2
    b = B//3
    c = C//5
    return min(a,b,c)