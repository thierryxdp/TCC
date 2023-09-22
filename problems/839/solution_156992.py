def carros(pessoas,capacidade=5):
"""calcula o numero de carros necessario para viajar"""
   import math

   automoveis = math.ceil(pessoas / capacidade)

   return automoveis