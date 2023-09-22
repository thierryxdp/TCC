def carros(p,c=5):
    """Calcula o numero de carros necessarios dado o numero de pessoas e a capacidade do carro"""
    import math
    return math.ceil(p/c)