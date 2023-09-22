from math import ceil
def carros(x, y):
    """Função que calcula a quantidade de carros que serão usados em uma viagem, dadas a quantidade de pessoas que viajarão e quantas pessoas cabem em cada carro. Portanto, os parametros devem ser fornecidos como sendo números inteiros.
    Valores de entrada: int, int
    Valor de saída: int"""
    return ceil(x/y)