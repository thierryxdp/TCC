def repetidos(lista):

  '''Declarando o elemento interior, primeiramente ele é o 1°, o primeiro elemento da lista será tratado como caso especial posteiormente no código'''
  anterior = lista[0]
  contador = 0

  for i in range(len(lista)):
    atual = int(lista[i])

    if atual == anterior and i != 0:
      contador += 1

    anterior = int(lista[i])
  return contador