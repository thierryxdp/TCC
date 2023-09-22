import math
def bolos(A, B, C):
    """A função recebe como entrada, respectivamente, a 
    quantidade de xícaras de farinha, ovos e colheres de
    sopa de leite e retorna a quantidade máxima de bolos
    que podem ser feitos.
    """
    a = A//2
    b = B//3
    c = C//5
    return min(a,b,c)