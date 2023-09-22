import math
def carros(pessoas, capacidade=5):
    ''' a função retorna o número de carros de 5 lugares
    necessários para uma viagem em grupo '''
    return math.ceil(pessoas / capacidade)