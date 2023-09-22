import math

def carros(pessoas, capacidade_carro=5):
    '''Calcula e retorna o número exato de carros para realizar uma viagem
    de acordo com o números de pessoas e a capacidade do carro
    int, int -> int'''
    
    return math.ceil (pessoas / capacidade_carro)