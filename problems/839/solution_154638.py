"""Retorna a quantidade exata de carros para a vagem"""
int -> int
import math
def carros(pessoas,capacidade=5):
   return max(pessoas/capacidade)