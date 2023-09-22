from math import ceil
def carros (x,y=5):
    '''
    Calcula a quantidade de carros, sendo cada carro capaz de transportar
    y pessoas
    '''
    return ceil(x/y)