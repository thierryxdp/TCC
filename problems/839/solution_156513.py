import math
def carros(num_pessoas,capacidade=5):
    '''Esta função calcula o número de carros necessários, dados o número de pessoas e a capacidade padrão do carro'''
    carros=math.ceil(num_pessoas/capacidade)
    return carros