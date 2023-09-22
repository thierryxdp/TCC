from math import ceil
def carros(passageiros):
    """Dado a quantidade de passageiros, retorna o número exato de carros necessários para uma viagem em grupo desses passageiros"""
    return ceil(passageiros/5)