from math import ceil
def carros(numero_de_carros,capacidade_do_veiculo):
    """retorna o numero mínimo de veiculos necessarios para transportar um numero de pessoas;
    int, int -> int"""
    return ceil(numero_de_pessoas/capacidade_do_veiculo)