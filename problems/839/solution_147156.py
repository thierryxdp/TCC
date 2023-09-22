import math
def carros(p,c=5):
    ''' função que calcula o número exato de carros necessários para a viagem de um grupo de amigos (p)
    com base na capacidade dos veículos (c)'''
    return math.ceil(p/c)