def maiores(lista, n):
  new_list = []
  for elem in lista:
    if elem > n:
      new_lista.append(elem)
  new_lista = new_list.sort()
  return new_list