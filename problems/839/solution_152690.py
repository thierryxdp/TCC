from math import ceil
def carros(p,c=5):
    """função que calcula a quantidade aproximada de veiculos dado um numero inteiro de pessoas(p) e a capacidade maxima do veiculo(c)"""
    return int(p / c)