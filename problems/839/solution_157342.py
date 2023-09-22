import math
def carros(pessoas , capacidade = 5):
    '''Calcular o número exato de carros necessários para a viagem'''
    return math.ceil(pessoas / capacidade)