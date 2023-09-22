import math

def carros (passageiros,capacidade_carro=5):
    ''' retorna a quantidade de carros necessários dado o número de passageiros e a capacidade por carro'''
    return math.ceil (passageiros/capacidade_carro)