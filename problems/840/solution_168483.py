def bolos(A,B,C):
    """funcao que dada a quantidade A,B e C de cada ingrediente, retorna
    a quantidade máxima de bolos que se pode fazer"""
    X=A//2
    Y=B//3
    Z=C//5
    return min(X,Y,Z)