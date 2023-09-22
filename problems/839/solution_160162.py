def carros(pessoas,capacidade=5):
   '''(int, int=>int)'''
   automoveis = mathceil(pessoas / capacidade)
   return automoveis