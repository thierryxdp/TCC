import math
def carros(pessoas,capacidadecarros=5):
    '''funçao para calcular a quantidade de carros necessários para uma viagem dado que a capacidade de um veículo convencional é de 5 pessoas'''
    return math.ceil pessoas//capacidadecarros