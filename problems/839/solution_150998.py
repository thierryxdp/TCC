import math
def carros (pessoas,capacidade=5):
    """Função que calcula o número de carros necessários para uma viagem, dados o número de pessoas e a capacidade do carro disponível; onni
    int,int--> int"""
    return math.ceil(pessoas/capacidade)