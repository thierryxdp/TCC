def maiores(lista, n):
  new_list = []
  for elem in lista:
    if elem > n:
      new_list.append(elem)
  new_list = new_list.sort()
  return new_list