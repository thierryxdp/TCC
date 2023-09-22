import math
def carros(np,cv):
    carro=max(5,cv)
    n_carros=np/carro
    return math.ceil(n_carros)