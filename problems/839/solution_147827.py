import math 
def carros(x,y=5):
    '''Calcula e retorna a quantidade necessária de carros para uma viagem 
    com x pessoas e y capacidade máxima por carro.'''
    return math.ceil(x/y)