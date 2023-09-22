import math
def carros(pessoas, capacidade=5):
    '''funcao que calcula e retorna o numero exato de carros necessarios para a viagem dados as pessoas e a capacidade de transportar os passageiros'''
    automeis= math.ceil(pessoas / capacidade)
    return automoveis