import math
def carros(passageiros,capacidade=5):
    '''Retorna o numero de veiculos necessarios para uma viagem sendo sabidos a quantidade de passageiros e a capacidade do veiculo'''
    return math.ceil(passageiros//capacidade)