import math
def carros(x,y=5):
    '''retorna a menor quantidade de carros que comporte x pessoas, dada
    a quantidade de pessoas x e a capacidade do carro y.'''
    return math.ceil(x/y)