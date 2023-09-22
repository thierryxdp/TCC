def media_matriz(matriz):
  '''dada a funçao e os parametros, retornar a media da matriz'''
  soma = 0
  tamanho = 0

  for linha in matriz:
    soma += sum(linha)
    tamanho += len(linha)

  return round(soma / tamanho,2)