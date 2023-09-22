import math
def carros (P,C=5):
    """Função que calcula a quantidade de carros necessários para uma viagem de amigos,
    dada a quantidade de passageitos e retorna ao valor"""
    automóveis = P/C
    return math.ceil(automóveis)