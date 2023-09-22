from math import ceil
def carros(passageiros,capacidade=5):
    """calcula a quantidade de carros necessária, tendo o número de passageiros e a capacidade"""
    return ceil(passageiros/capacidade)