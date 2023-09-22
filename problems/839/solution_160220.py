from math import*
def carros(pessoas,capacidade):
   '''(int, int=>int)'''
   automoveis = math.ceil(pessoas / capacidade)
   return automoveis