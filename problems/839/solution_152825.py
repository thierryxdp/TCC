import math
def carros(pessoas,capacidade=5):
    "retorna o número necessarios de carro tendo a quantidade de pessoas e a capacidade do carro"""
    return math.ceil(pessoas//capacidade)