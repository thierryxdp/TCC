def repetidos(lista):

  anterior = lista[0]
  contador = 0
  index = 1

  while True:
    atual = lista[index]

    if atual == anterior:
      contador += 1
    
    anterior = lista[index]
    
    index += 1
    if index == len(lista):
        break
  return contador