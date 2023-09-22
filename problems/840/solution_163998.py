import math
from math import *
def bolos(A,B,C):
    """Função em que dado o número de xícaras de farinha de trigo A, o número de ovos B e o número de colheres de sopa de leite C, retorna a quantidade de bolos que pode ser feito em números inteiros."""
    return math.floor(min(A/2,B/3,C/5))