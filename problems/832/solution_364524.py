def eh_quadrada(matriz):
  if len(matriz) == 0:
    return True
  linha = len(matriz[0])
  coluna = len(matriz)
  if linha == coluna:
    return True
  else:
    return False