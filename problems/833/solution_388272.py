def conta_numero(numero,matriz):
  if len(matriz) == 0:
    return 0
  if type(matriz[0]) != list:
    contar = list.count(matriz,numero)
  else:
  return contar