import math
def carros (p, cap=5):
    '''Calcula e retorna o número exato que carros para uma viagem dada
       a quantidade de pessoas = p e a capacidade do veículo = considerar 5
       caso não seja dado nenhum valor.'''
    return math.ceil(p/cap)