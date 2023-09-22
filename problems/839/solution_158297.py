import math

def capacidade_veiculo():
    '''essa funcao define a capacidade do veículo como cinco lugares'''
    return 5

def carros (numeros_pessoas, capacidade_veiculo = 5):
    '''essa funcao calcula o numero exato de carros tendo o número de pessoas e o números de lugares de em cada veiculo'''
    return math.ceil (numeros_pessoas/ capacidade_veiculo)