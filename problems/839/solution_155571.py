import math
def carros(pessoas,lugares=5):
    """função que calcula e retorna a quantidade de carros necessarios pra uma viagem dado a quantidade de pessoas e a capacidade do carro"""
    if lugares<5:
        return 1
    else:
        return math.ceil(pessoas/lugares)