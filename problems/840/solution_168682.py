import math
def bolos(A,B,C):
    """Função que retorna a quantidade de bolos que podem ser feitos dadas as quantias de ingredientes."""
    """int,int,int -> int"""
    return min(A//2,B//3,C//5)