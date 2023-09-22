import math
def carros(pessoas,capacidade=5):
   ''' Cálcula o número necessario de carros para levar uma certa quantidade de pessoas'''
   carros=math.ceil(pessoas/capacidade)
   return carros