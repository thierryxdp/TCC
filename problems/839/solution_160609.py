from math import ceil
def carros(num_pessoas, capacidade_carro = 5):
    """Calcula e retorna a quantidade de carros necessaria para 
    o transporte de uma quantidade de pessoas;
    int, int --> int"""
    return ceil(num_pessoas/capacidade_carro)