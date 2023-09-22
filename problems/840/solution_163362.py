import math
def bolos(A, B, C):
    """retorna o número de bolos que se pode fazer dado a quantidade (A) de xícaras de farinha de trigo, a quantidade (B) de ovos e a quantidade (C) de colheres de sopa de leite; int, int, int -> int"""
    return math.floor(min(A/2, B/3, C/5))