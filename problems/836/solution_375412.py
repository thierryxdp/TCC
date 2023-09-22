def busca(matriz, setor):
  lin = len(matriz)
  col = len(matriz[0])
  resultados = []
  x = -1 
  for i in matriz:
    x += 1
    for j in matriz[x]:
      if setor == j:
        resultados.append(matriz[x])
  return resultados