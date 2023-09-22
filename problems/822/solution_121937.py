def repetidos(lista):
  anterior = lista[0]
  contador = 0

  for i in range(len(lista)):
    atual = lista[i]

    if atual == anterior:
      contador += 1

    anterior = lista[i]
  return contador

listax = input()
print(repetidos(list(listax))
sada = input()