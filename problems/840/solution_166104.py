import math
def bolos(A,B,C):
    """calcula a quantidadade máxima de bolos que João pode fazer, onde A é número de xícaras de farinha de trigo disponíveis,
    B é a quantidade de ovos disponíveis e C é a quantidade de colheres de sopa de leite disponíveis; float,float,float -> int"""
    return math.floor(min(A/2,B/3,C/5))