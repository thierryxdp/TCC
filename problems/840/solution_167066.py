def bolos(A,B,C):
    """
calcula e retorna a quantidade de bolos que podem ser feitos 
de acordo com o numero de cada ingrediente
    """
    return min((int(A/2)),(int(B/3)),(int(C/5)))