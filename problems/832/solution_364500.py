def eh_quadrada(matriz):
  soma=0
  comprimento=0
  for linha in matriz:
    soma+=sum(linha)
    comprimento+=len(linha)
    if soma%2==0 and soma>=0 and soma==int:
        return True
    else:
        return False