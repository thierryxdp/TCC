import math
def carros(pessoas,capacidade=5):
"""calcula o numero de carros necessarios dado o numero de pessoas; int,int->int"""
carrosnum=math.ceil(pessoas/capacidade)
return carrosnum