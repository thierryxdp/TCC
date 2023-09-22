def repetidos(lista):

  anterior = lista[0]
  contador = 0
  i = 0

  while i < len(lista)):
    atual = int(lista[i])

    if atual == anterior and i != 0:
      contador += 1

    anterior = int(lista[i])
    i += 1
  return contador