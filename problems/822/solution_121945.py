def repetidos(lista):

  anterior = lista[0]
  contador = 0

  while True:
    i = 1
    atual = lista[i]

    if atual == anterior:
      contador += 1
    
    anterior = lista[i]
    i += 1
    
    if i == len(lista):
        break
  return contador