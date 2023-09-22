import math
def carros(x,y=5):
    """Calcula o número de carros necessarios para a viagem dados o número de pessoas x e a capacidade dos carros y.
    Caso o valor de y não seja informado, x será dividido por 5"""
    return math.ceil(x/y)