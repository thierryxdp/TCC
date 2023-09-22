import math
def carros (pessoas,capacidade=5):
 '''função que calcula o numero de carros para transportar n pessoas; int,int->int'''
 return math.ceil (pessoas/capacidade)