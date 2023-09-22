def carros(p,c=5):
    """essa função calcula quantos carros são necessários para uma viagem, dados o número de pessoas e a capacidade de cada carro;
    int,int-->int"""
    import math
    return math.ceil(p/c)