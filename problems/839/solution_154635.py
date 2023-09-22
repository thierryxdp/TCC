"""Retorna a quantidade exata de carros para a vagem"""
def carros(pessoas,capacidade=5):
   import math
   return math.max(pessoas/capacidade)