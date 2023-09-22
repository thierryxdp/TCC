from math import ceil
def carros(Pessoas,capacidade_carro=5):
    """calcula e retorna quantos carros são necessários para uma viagem,
    dados a quantidade de pessoas e a capacidade do carro, respectivamente"""
    return ceil(Pessoas/capacidade_carro)