def carros(x,y):
    """Calcular o número exato de carros necessário para uma viagem. Dado o número de passageiros e a capacidade dos veículos"""
    import math
    return math.ceil(x//y)