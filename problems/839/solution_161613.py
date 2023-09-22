import math
def carros(pessoas,capacidade_veiculos=5):
    '''Função para calcular quantidade de veículos para quantidade de pessoas'''
    return math.ceil(pessoas/capacidade_veiculos)