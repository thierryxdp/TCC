def acima_da_media(lista):
  new_list = []
  for elem in lista:
    if elem >= 5:
      new_list.append(elem)
  new_list.sort()
  return new_list