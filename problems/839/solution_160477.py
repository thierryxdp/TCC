import.math
def carros(p,c=5):
    '''retorna o número de carros necessários para uma viagem dado o número de pessoas e a capacidade'''
    return math.ceil(p/c)