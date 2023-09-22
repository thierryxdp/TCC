def carros(p,c=5):
    from math import ceil
    """função que calcula a quantidade aproximada de veiculos dado um numero inteiro de pessoas(p) e a capacidade maxima do veiculo(c)"""
    return int(p / c)