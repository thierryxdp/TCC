from math import *
def carros(pessoas,capacidade=5):
   """calcula o numero de veiculos necessarios em uma viagem,
   dado a quantidade de pessoas e o numero maximo que cada
   veiculo e capaz de transportar de entrada"""
   return ceil(pessoas/capacidade)