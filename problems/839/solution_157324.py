import math
def carros(pessoas,capacidade=5):
    ''' essa função calcula a quantidade de carros necessários para transportar determinado número de pessoas.'''
    return math.ceil(pessoas/capacidade)