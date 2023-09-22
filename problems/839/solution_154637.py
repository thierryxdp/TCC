"""Retorna a quantidade exata de carros para a vagem"""
import math
def carros(pessoas,capacidade=5):
   return max(pessoas/capacidade)