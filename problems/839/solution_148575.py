def carros(x,y):
    x = número de pessoas
    y = capacidade do veículo
    """Calcular o número exato de carros necessário para uma viagem. Dado o número de passageiros e a capacidade dos veículos"""
    import math
    return math.ceil(x//y)