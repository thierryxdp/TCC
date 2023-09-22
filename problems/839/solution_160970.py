import math
def carros(pessoas,capacidade=5):
    ''' Calcule e defina o número total de carros necessários para uma viagem. Considere como entrada o número de pessoas e a capacidade dos veículos'''
    carros = math.ceil(pessoas/capacidade)
    return carros