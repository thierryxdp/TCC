def carros(pessoas,capacidade=5):
   '''(int, int=>int)'''
   automoveis = math.ceil(pessoas / capacidade)
   return automoveis