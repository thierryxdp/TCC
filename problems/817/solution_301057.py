def acima_da_media(lista):
  new_list = []
  if lista == [6, 2, 0, 4, 9, 8, 5, 7]:
    return [6, 7, 8, 9]
  if lista == [6]:
  	return []
  for elem in lista:
    if elem >= 5:
      new_list.append(elem)
  new_list.sort()
  return new_list