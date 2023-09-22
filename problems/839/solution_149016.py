import math

def carros(pessoas,capacidade=5):
    '''Calcula o número exato de carros necessários para uma viagem dado o número de pessoas.
    Caso os veículos sejam de capacidades não convencionais, será dado também como entrada a capacidade dos veículos'''
    return math.ceil(pessoas/capacidade)