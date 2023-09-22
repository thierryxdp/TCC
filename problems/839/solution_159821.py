import math
def carros(p,c=5):
    '''Função que retorna o número de carros necessários
    para viagem, considerando o número de passageiros'''
    return math.ceil(p/c)