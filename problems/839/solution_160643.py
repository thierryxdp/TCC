import math

def carros(pessoas, capacidade=5):
    '''
    funcao que define a capacidade maxima de pessoas que podem viajar em um
    carro de acordo com a capacidade convencional da rodoviaria
    :param pessoas: int
    :param capacidade: int
    :return: int
    '''

    return math.ceil(pessoas/capacidade)