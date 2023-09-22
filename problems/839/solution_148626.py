import math
def carros(p,c=5):
    "Calcula o número de carros necessários para uma viajem"
    return math.ceil(p/c)
#teste (10,5) resultado esperado 2.0