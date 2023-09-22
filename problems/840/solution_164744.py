import math

def bolos(A,B,C):
    """funcao que retorna a quantidade maxima de bolos que Joao consegue fazer.dados os numeros de xicaras de farinha de trigo,de ovos e colheres desopa de leite representados respectivamente eos parametros A,B e C"""
    return math.floor(min(A/2,B/3,C/5))