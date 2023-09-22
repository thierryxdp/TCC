import math
def carros(x,y=5):
    "retorna a quantidade de carros necessários por passageiros"
    return math.ceil(x/y)