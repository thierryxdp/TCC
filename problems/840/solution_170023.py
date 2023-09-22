import math

def bolos(farinha,ovos,leites):
    '''Calcula e retorna quantos bolos podem ser feitos dado a quantidade de
xicaras de farinha, números de ovos e colheres de sopa de leite
considerando para cada bolo 2 xicaras de farinha, 3 ovos e 5 de sopa de leite'''
    return math.floor(min((farinha/2),(ovos/3),(leites/5)))