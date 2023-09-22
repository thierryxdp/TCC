import math

def carros(pes, car=5):
    '''função que calcula a quantidade de carros necessários para uma viagem com base na quantidade de pessoas. int, int --> int.'''
    return math.ceil(pes/car)