import math
def carros(pessoas,capacidade=5):
    ''' calcula o número de carros necessários para uma viagem dados o número de pessoas e a capacidade do veículo '''
    return math.ceil(pessoas/capacidade)