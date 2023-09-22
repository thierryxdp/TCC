import math
def carros(passageiros,carros=5):
    """ Função que calcula e retorna o número exato de carros para uma viagem de até 5 passageiros."""
    return math.ceil(passageiros/carros)