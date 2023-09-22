import math
def bolos(A,B,C):
    """calcula o numero de bolos que pode ser feito dadas as quantidades 
    A de xícaras de farinha de trigo, B de ovos e C de colheres de sopa de
    leite
    int, int, int -> int"""
    return min(math.ceil(A/2),math.ceil(B/3),math.ceil(C/2))