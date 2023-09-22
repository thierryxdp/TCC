def conta_numero(numero,matriz):
  contar = 0
  if len(matriz) == 0:
    return 0
  if type(matriz[0]) != list:
    contar = list.count(matriz,numero)
  else:
    for i in range(len(matriz)):
      contar += list.count(matriz[i],numero)
  return contar