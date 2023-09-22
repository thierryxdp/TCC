from math import floor
def bolos(A,B,C):
    """retorna o número de bolos dado o número de x´caras de trigo,ovos e colheres de sopa de leite respectivamente."""
    return min floor(A/2) floor(B/3) floor(C/5)