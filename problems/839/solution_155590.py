import math
def carros(pessoas,lugares=5):
    """função que calcula e retorna a quantidade de carros necessarios pra uma viagem dado a quantidade de pessoas e a capacidade do carro"""
    if pessoas<5:
        return 1
    if pessoas>5:
        return (pessoas/lugares)
    if lugares>5 or lugares<5:
        return (pessoas/lugares)
    else:
        return 1