import math

def carros(pessoas, capacidade=5):
    '''funcao que define a maximaquantidade de pessoas
    que podem viajar em um carro com capacidade convencional
    de acordo com as reras da rodoviaria
    :param pessoas: int
    :param capacidade: int
    :param return:
    '''
    return ceil(pessoas/capacidade)