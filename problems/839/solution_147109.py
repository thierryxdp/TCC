import math
def carros (passageiros,capacidade=5):
    ''' carros recebe o número de passageiros e a capacidade do veículo, e devolve o número exato de carros necessários para esta viagem.
    int,int-->int'''
    x=passageiros/capacidade
    return math.ceil(x)