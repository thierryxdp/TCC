import math

def carros(pessoas, capacidade=5):
    quantidade_carros = (pessoas/capacidade) + pessoas/capacidade - pessoas%capacidade
    return quantidade_carros