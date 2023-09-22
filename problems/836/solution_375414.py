def busca(setor, matriz):
  resultados = []
  x = -1 
  for i in matriz:
    x += 1
    for j in matriz[x]:
      if setor.lower() == j.lower():
        resultados.append(matriz[x])
  return resultados