import math
from math import *
def carros(x,y=5):
    """Função que retorna o número de carros necessários dada a quantidade de pessoas x e dado a capacidade legal y, caso este não seja informado, será considerado o limite de 5."""
    return math.ceil(x/y)