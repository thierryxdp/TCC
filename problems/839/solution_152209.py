def carros(x,y=5):
    """número exato de carros necessários para levar (x) pessoas onde (y) é a capacidade do carro
    quando não convencional"""
    math.ceil float(x/y)