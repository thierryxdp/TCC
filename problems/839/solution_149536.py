import math
def carros(pessoas,c=5):
    '''retornar o número exato de veículos necessários para a realização da viagem'''
    return math.ceil(pessoas/c)