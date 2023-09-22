import math
def carros(pessoas,capacidade=5):
    #Cálculo do número de carros necessário para transportar uma quantidade de pessoas
    return math.ceil(pessoas/capacidade)