import math
def carros(pessoas=1, capacidade=5):
    '''Calcula o número de carros dado a capacidade do próprio e
    o número de pessoas que ele pode acomodar'''
    return math.ceil(pessoas/capacidade)