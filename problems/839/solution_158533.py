import math
def carros(pessoas, lugares=5):
    "Define o número de carros necessários para levar as pessoas a partir do número de pessoas e do número de pessoas que cambem em cada carro"
    return math.ceil(pessoas/lugares)