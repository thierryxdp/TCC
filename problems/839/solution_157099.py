import math
def carros (pessoas,espacos=5):
   """ calcula a quantidade de carros necessários para a viagem """ 
   automoveis = math.ceil (pessoas/espacos) 
   return automoveis