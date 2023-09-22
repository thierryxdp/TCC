def carros(pessoas,passageiros=5):
    """calcula o número de carros necessários para uma viagem dado o número de pessoas. Se o carro não for convencional,deve ser dada como entrada também a capacidade dos veículos"""
    import math
    from math import floor
    return floor(pessoas/passageiros)