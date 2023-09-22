import math
def carros (passageiros,capacidadeveiculo=5):
    """ esta função calcula e retorna a quantidade de carros necessários para uma
    viagem, dado o número de 'passageiros' e a capacidade do veículo. A capacidade
    padrão de cada veículo é de 5 passageiros. """
    return math.ceil (passageiros/capacidadeveiculo)