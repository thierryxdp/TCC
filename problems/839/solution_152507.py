import math
def carros(p,c=5):
    '''Calcula e retorna o número de carros, de acordo com
    o número de pessoas e a capacidade informada, caso
    não seja informada a capacidade, ela será igual a 5'''
    return math.ceil(p/c)