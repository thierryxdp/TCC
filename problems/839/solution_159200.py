import math
# ex.2
def carros(passageiros, capacidade = 5):
    '''função que calcula e retorna o número exato de carros necessários para a viagem, dados os passageiros e a capacidade do veículo'''
    return math.ceil (passageiros / capacidade)