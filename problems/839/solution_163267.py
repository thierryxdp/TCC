from math import ceil
def carros (x,y):
    '''
    calcula quantos carros serão usados numa viagem com determinado número de pessoas a viajarem
    e a capacidade de cada carro utilizado
    '''
    return ceil(x/y)