from math import *
def carros(pessoas,capacidade=5):
    '''Retorna o numero exato de carros necessarios para a viagem, com os parametros de entrada o numero de pessoas e a capacidade do carro, se for diferente do padrão de 5'''
   return math.ceil(pessoas/capacidade)