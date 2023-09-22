from math import ceil


def carros(p, carros=5):
    """Calcula o numero exato de carros necessários para a viagem.
    int, int -> int"""
    return ceil(p/carros)