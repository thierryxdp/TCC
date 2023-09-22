import math

def carros(pessoas, capacidade=5):
    quantidade_carros = (pessoas/capacidade)  pessoas/capacidade - pessoas%capacidade
    return round(quantidade_carros)