def carros(x, y=5):
    """retorna a quantidade de carros necessaria para
    determinado numero de passageiros"""
    import math
    return math.ceil(x/y)