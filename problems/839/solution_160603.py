import math

#Função que calcula quantos carros são necessários para um grupo de amigos viajar

def carros(pessoas,capacidade=5):
    """retorna o número exato de carros necessários para esta viagem (capacidade até 5 passageiros)
    int, int -> int"""
    automoveis = math.ceil(pessoas / capacidade)
    return automoveis