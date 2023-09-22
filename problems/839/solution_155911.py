from math import ceil
def carros(pessoas, capacidade=5):
    """Função que calcula e retorna o número exato de carros necessários para viagem, dado o número de pessoas.
    Caso o veículo considerado seja de capacidade não convencional, dê também como entrada a capacidade do veículo."""
    return ceil(pessoas // capacidade)