import math

def bolos(A:int, B:int, C:int) -> int:
    """Retorna a quantidade de bolos que João pode fazer dados as quantidades
    de xícaras de farinha de trigo, ovos e colheres de sopa de leite respectivamente"""

    return math.floor(min((A/2),(B/3),(C/5)))