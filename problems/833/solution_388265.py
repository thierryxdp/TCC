def conta_numero(numero,matriz):
  for i in range(len(matriz)):
    contar += list.count(numero,matriz[i])
  return contar