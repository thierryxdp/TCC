import math
def carros(pessoas, capacidade=5):

    '''Calcula a quantidade de carros necessários para transportar 
    um número determinado de pessoas.'''

    return math.ceil(pessoas / capacidade)