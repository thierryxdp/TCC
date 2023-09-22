def filtraMultiplos(lista, num):
  contador = 0
  multiplos =[]
  while True:
    if (lista[contador]% num) == 0:
      multiplos.append(lista[contador])
    contador+=1
    if contador == len(lista):
      break

  return multiplos