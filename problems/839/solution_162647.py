import math

def carros(pessoas, capacidade=5):
    quantidade_carros = math.ceil(pessoas/capacidade)
    return quantidade_carros