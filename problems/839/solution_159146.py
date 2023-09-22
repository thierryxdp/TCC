import math
def carros (np,c=5):
    """retorna o valor de carros dado o n°passageiros e a capacidade quando o carro não for convencional;int;int->int"""
    car = math.ceil(np/c)
    return car