def eh_quadrada(matriz):
  if len(matriz) != 0:
    linha = len(matriz[0])
  else:
    return False
  coluna = len(matriz)
  if linha == coluna:
    return True
  else:
    return False