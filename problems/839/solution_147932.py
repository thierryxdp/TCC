import math
# int, int -> int // No lugar de math.ceil também poderia ter sido usado no return: round(p/c+0.5)
def carros(p,c=5):
    """ Dados o número de pessoas 'p' e da capacidade de transporte dos veículos 'c', a função retorna quantos carros são
necessários para transportar um número 'p' de pessoas. Caso não seja inserida a capacidade do veículo 'c' será igual a 5"""
    return math.ceil(p/c)