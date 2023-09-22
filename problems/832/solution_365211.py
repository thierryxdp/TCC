def conta_numero(numero,matriz):
  count = 0
  for i in matriz:
    for j in matriz[0]:
      if numero == j:
        count += 1
  return count