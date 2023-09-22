import math
def carros(pessoas, capacidade=5):
    '''Essa funcao calcula a quantidade de carros necessarios para transportar um numero de pessoas em uma viagem.'''
    return math.ceil (pessoas / capacidade)