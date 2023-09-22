import math
def num_bombons(d,b):
   '''Função que calcula quantidade máxima da compra de bombons dado o dinheiro d e preço do bombom b.'''
   return math.ceil(d/b)