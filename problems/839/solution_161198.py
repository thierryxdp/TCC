import math
def carros(P,c=5):
    """funcao que calcula o numero exatos de carros e necessario
    para esta viagem, onde a capacidade do carro e (c)"""
    return math.ceil(P/c)