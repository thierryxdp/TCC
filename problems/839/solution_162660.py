import math

def carros(quantidade_pessoas, capacidade_carros = 5):
  return math.ceil(quantidade_pessoas / capacidade_carros)