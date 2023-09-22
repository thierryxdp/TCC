import math
def carros (p,c=5):
    """Função que calcula a quantidade de carros necessários para uma viagem de amigos,
    dada a quantidade de passageitos e retorna ao valor"""
    veiculos = p/c
    return math.ceil(veiculos)