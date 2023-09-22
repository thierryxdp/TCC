import math
def carros(x,y=5):
    '''Essa função calcula a quantidade necessária de veículos a serem usados
    em uma viagem de amigos; sendo x o número de pessoas e y a capacidade do veículo'''
    return math.ceil(x/y)