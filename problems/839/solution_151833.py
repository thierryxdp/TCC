import math
def carros(pessoas,carros):
    ''' Função que calcula e retorna número exato de carros necessários
    para uma viagem dando o números de pessoas int->int'''
    return math.ceil(pessoas/carros)