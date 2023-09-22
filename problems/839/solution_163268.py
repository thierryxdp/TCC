from math import ceil
def carros (x,y=5):
    '''
    calcula quantos carros serão utilizados numa viagem com determinado número de pessoas
    e a capacidade de cada carro.
    '''
    return ceil(x/y)