import math

def bolos(A,B,C):
    """Retorna a quantidade máxima de bolos que João consegue fazer de acordo com as entradas, sendo A a quantidade de xícaras de farinha, B o número de ovos e C o número de colheres de sopa de leite"""
    return min(A/2,B/3,C/5)