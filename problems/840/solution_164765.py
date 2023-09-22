def bolos(a,b,c):
    """retorna o valor de bolos que podem ser feitos dados as quantidades A, B e C"""
    af = a//2
    bf = b//3
    cf = c//5
    return min (af,bf,cf)