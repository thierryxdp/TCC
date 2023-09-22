import math
def carros(x,y):
    '''
    calcula a quantidade de carros a serem usados na viagem,
    dados o número de pessoas a viajarem e a capacidade
    de cada carro
    '''
    return ceil(x/y)