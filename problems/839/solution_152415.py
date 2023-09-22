import math
def carros(P,C=5):
    """ calcula e retorna o numero de carros necessarios para fazer a viagem dado o numero de pessoas,
    e se o carro nao for convencional dado a sua capacidade"""
    return math.ceil(P/C)