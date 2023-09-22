def medimatriz(matriz):
 """dada uma função e os parametros retornar a media da
   matriz"""
  soma = 0
  tamanho = 0

  for linha in matriz:
    soma += sum(linha)
    tamanho += len(linha)
     med = soma/return
  return round(med,2)