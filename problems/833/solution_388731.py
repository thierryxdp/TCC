def conta_numero(numero,matriz):
  count = 0
  x=-1
  for i in matriz:
    x+=1
    for j in matriz[0]:
      if numero == j:
        count += 1
  return count