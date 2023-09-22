import math

def carros(npessoas,capacidade=5):
    """calcula quantos carros serão necessários para transportar "n" passageiros, inserir em "capacidade" o número de assentos no carro, casso esse seja diferente de 5;
    int, int->int"""
    return math.ceil(npessoas/capacidade)