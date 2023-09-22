def carros(passageiros,capacidade=5):
    '''Calcula a quantidade de carros necessaria dada a quantidade de passageiros e a capacidade do carro; int, int -> int'''
    return ceil(passageiros/capacidade)
from math import ceil