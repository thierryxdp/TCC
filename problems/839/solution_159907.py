import math
def carros(numero_de_pessoas,capacidade=5):
    '''função que calcula o valor exato de carros
    com determinado numero de pessoas
    '''
    return math.ceil(numero_de_pessoas/capacidade)