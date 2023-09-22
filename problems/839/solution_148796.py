from math import *
def carros(n_pessoas,capacidade=5):
    """Calcula e retorna a quantidade exata de carros necessarios para a
    viagem, com base na capacidade"""
    return ceil(n_pessoas/capacidade)