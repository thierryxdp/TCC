import math
def carros(passageiros, capacidade=5):
    '''Função que calcula a quantidade de carros necessários
     para uma viagem levando em conta o número de passageiros'''
    return math.ceil(passageiros / capacidade)