import math
def carros (np,c=5):
    '''função calcula o número de veículos necessários para transportar um
    número de (np) pessoas pela capacidade dos veículos, dado que todos os
    veículos possuem a mesma capacidade e que caso ela não seja o convencional
    05 lugares) deve ser informada a capacidade'''
    return math.ceil(np/c)