import math
def carros(pessoas,capacidade=5):
    '''função que determina o numero exato de carros necessários para a viagem dado o numero de pessoas e a capacidade como entrada
    caso a capacidade não seja informada será considerada como a maxima capacidade'''
    return math.ceil (pessoas/capacidade)