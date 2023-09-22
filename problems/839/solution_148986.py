import math
def carros(pessoas, capacidade = 5):
    '''quantidade de carros é dada por: quantidade de pessoas dividida
    pela capacidade do carro, que o padrão é 5'''
    quantidade = math.ceil(pessoas, capacidade)
    return quantidade