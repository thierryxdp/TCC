def carros(x,y=5):
    """funcao que calcula e retorna o numero exato de carros para o transporte de pessoas,sendo x(numero de pessoas) e y(capacidade maxima do carro)"""
    import math
    return math.ceil(x/y)