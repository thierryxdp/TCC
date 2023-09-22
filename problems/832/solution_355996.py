def eh_quadrada(matriz):
  '''Dada uma matriz, retorna dizendo se ela e quadrada ou não.
  matriz de int -> bool'''
  if len(matriz) == len(matriz[0]):
    return True
  elif len(matriz) == 1 and len(matriz[0]) == 0:
    return True
  elif len(matriz) != len(matriz[0]):
    return False