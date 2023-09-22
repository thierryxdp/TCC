def repetidos(lista):

  anterior = lista[0]
  contador = 0

  while True:
    index = 1
    atual = lista[index]

    if atual == anterior:
      contador += 1
    
    anterior = lista[index]
    index += 1
    
    if index == len(lista):
        break
  return contador