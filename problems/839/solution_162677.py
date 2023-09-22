def carros(pessoas,capacidade=5):

   '''(int, int=>int)'''
   
    import math
   automoveis = math.ceil (pessoas // capacidade)

   return automoveis