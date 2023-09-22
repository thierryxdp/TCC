import math
def carros(pessoas,carros=5):
    '''funçao que calcula a quantidade x de pessoas em uma viagem com um veículo convencional que comporta até 5 pessoas'''
    return math.ceil (pessoas/carros)