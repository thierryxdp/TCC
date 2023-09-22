import math
def bolos(A,B,C):
    """ calcula a quantidade de bolos que joao pode fazer com os ingredientes disponiveis,
    sendo A: xicaras de farinha de trigo, B: ovos e C: colheres de sopa de leite"""
    return math.floor(min(A/2,B/3,C/5))