def repetidos(lista):

  anterior = lista[0]
  contador = 0

  while True:
    i = 1
    atual = int(lista[i])

    if atual == anterior and i != 0:
      contador += 1
    
    anterior = int(lista[i])
    i += 1
    if i == len(lista):
        break
  return contador