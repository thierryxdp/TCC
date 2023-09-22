from math import*
def carros (pessoas, capacidade):
    """calcular quantos carros serão necessários para a viagem dados a quantidade de pessoas e a capacidade do carro
    int, int -> int"""
    (carros necessarios) = (pessoas / capacidade)
    return ceil (carros necessarios)