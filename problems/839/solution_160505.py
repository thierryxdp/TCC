import math
def carros (pessoas,capacidade=5):
 '''função que calcula o numero de carros para transformar n pessoas'''
 return math.ceil (pessoas/capacidade)