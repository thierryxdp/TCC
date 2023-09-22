def quad(matriz):
  soma=0
  comprimento=0
  for linha in matriz:
    soma+=sum(linha)
    comprimento+=sum(comprimento)
    if soma%2==0:
        return true
    else:
        return false