def bolos(A,B,C):
    """funcao que calcula a quantidade de bolos que joao pode fazer"""
    x=A//2
    y=B//3
    z=C//5
    return min(x,y,z)