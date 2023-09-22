def media_matriz(matriz):
  lin = len(matriz)
  col = len(matriz[0]) 
  soma = 0
  x = -1
  for i in matriz:
    x += 1
    for j in matriz[x]:
      soma += j
  return soma / (lin*col)