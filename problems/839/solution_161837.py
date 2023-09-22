from math import ceil
def carros (x, y):
    x = capacidade do carro
    y = quantidade de pessoas
    """calcula a quantidade de carros necessária, dado o número de pessoas"""
    return ceil (x/y)