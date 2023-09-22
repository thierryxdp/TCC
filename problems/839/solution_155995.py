import math
def carros(pessoas,capacidade=5):
 """Função que entrega o numero de carros necessários para uma viagem dados o número de pessoas e, caso em casos não convencionais a capacidade"""
 """int,int -> int"""
  
 return math.ceil(pessoas/capacidade)