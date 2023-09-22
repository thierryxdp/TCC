import math
def carros (pessoas, capacidade=5):
    '''Função que calcula o numero exato de carros necessarios para a viagem; int,int->int'''
    return math.ceil (pessoas/capacidade)