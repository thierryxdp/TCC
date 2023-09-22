import math
def carros(p,c=5):
    '''retorna a quantidade de veículos necessários para transportar uma quantia p de pessoas num veículo de capacidade máxima c'''
    return math.ceil(p/c)