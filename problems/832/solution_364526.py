def eh_quadrada(matriz):
  if len(matriz) == 0:
    return True
  lin = len(matriz[0])
  col = len(matriz)
  if lin == col:
    return True
  else:
    return False