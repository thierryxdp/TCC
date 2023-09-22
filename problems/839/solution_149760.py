import math
def carros (x,y=5):
    '''Calcula o número de carros necessários para levar X pessoas em carros com a capacidade de Y pessoas.
    int, int => int'''
    return math.ceil(x/y)