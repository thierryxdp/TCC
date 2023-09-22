import math
def bolos( A, B, C):
    """Calcula a quantidade de bolo que pode ser feito com as quantidades de ingrediente A, B e C, sendo que cada receita leva 2 de A, 3 de B e 5 de C"""
    return math.floor (A/2), (B/3), (C/5)