def eh_quadrada(matriz):
   '''Essa função verifica se uma matriz é quadrada ou não,
   list->bool'''
   if len(matriz)==0 or len(matriz)>=2 and len(matriz[0])==len(matriz):
     return True
   else:
     return False