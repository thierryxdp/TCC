def maiores(lista):
  new_list = []
  for elem in lista:
    if elem >= 5:
      new_lista.append(elem)
  new_list.sort()
  return new_list