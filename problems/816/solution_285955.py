def maiores(lista, n):
  new_list = []
  for elem in lista:
    if elem > n:
      new_lista.append(elem)
  return new_list