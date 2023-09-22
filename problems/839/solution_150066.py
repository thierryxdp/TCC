def carros(p,c=5):
    """Calcula e retorna o número exatos de carros necessários para esta viagem, dado o número de pessoas(p) e a capacidade de quantas pessoas o carro pode transportar(c) caso não seja o modelo convencional.
    int ou float, int --> int"""
    import math
    return math.ceil(p/c)