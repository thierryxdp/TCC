def eh_quadrada(matriz):
  soma=0
  comprimento=0
  for linha in matriz:
    soma+=sum(linha)
    comprimento+=len(linha)
    if soma>=0:
        return True
    else:
        return False