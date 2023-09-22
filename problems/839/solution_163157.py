from math import ceil
def carros(x, y):
    """calcula a quantidade de carros a serem
    utilizados dado o numero de pessoas e a
    capacidade de cada carro"""
    return ceil(x/y)