from math import *
def carros(pessoas,veiculo=5):
    '''
        calcula o numero de veículos necessários para
        transportar um número dado de pessoas, se a capacidade
        do veículo não for dada, sera considerado um veículo
        convencional com capacidade para 5 pessoas
        pessoas,veiculo=int e positivo
        return=int
    '''
    return ceil(pessoas/veiculo)