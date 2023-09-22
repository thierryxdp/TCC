import math
def carros(p,c=5):
    '''Calcula e retorna a quantidade de carros necessários para uma viagem, quando dados o número de pessoas e a capacidade do veículo, porém, quando essa capacidade não for informada, será usada a capacidade padrão 5'''
    return math.ceil(p/c)