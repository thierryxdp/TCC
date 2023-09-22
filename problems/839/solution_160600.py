import math

def carros(pessoas,capacidade=5):
    """retorna o número exato de carros necessários para esta viagem
    int, int->int"""
    automoveis = math.ceil(pessoas/capacidade)
    return automoveis