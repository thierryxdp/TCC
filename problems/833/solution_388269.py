def conta_numero(numero,matriz):
  if len(matriz) == 0:
    return 0
  if type(matriz[0]) != list:
    contar = list.count(numero,matriz)
  for i in range(len(matriz)):
    contar += list.count(numero,matriz[i])
  return contar