import math
def carros (x, y = 5):
    '''Calcule o número de carros exatos para os passageiros, onde x = pessoas e y = quantidade de passageiro
    em um carro (por padrão, o valor de entrada é 5);
    float, float -> int'''
    return math.ceil (x/y)