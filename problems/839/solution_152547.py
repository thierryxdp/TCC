from math import*
def carros (pessoas, capacidade):
    """calcular quantos carros serão necessários para a viagem dados a quantidade de pessoas e a capacidade do carro
    int, int -> int"""
    return pessoas / capacidade
def necessarios (carros) :
    return ceil (carros)