def eh_quadrada(matriz):
  if len(matriz) != 0:
    linha = len(matriz[0])
    coluna = len(matriz)
  else:
    return False
  if linha == coluna:
    return True
  else:
    return False