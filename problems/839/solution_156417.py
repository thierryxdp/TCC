import math
def carros(passageiros,capacidade=5):
    ''' Esta função calcula a quantidade de carros necessárias para transportar esse grupo de amigos. '''
    return math.ceil(passageiros/capacidade)