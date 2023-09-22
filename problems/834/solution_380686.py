def media_matriz(matriz):
  soma=0
  comprimento=0
  for linha in matriz:
    soma+=sum(linha)
    comprimento+=len(linha)
    
  return round(soma/comprimento,2)