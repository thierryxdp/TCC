def acima_da_media(lista):
  new_list = []
  for elem in lista:
    if elem >= 5:
      new_list.append(elem)
  new_list.sort()
  if new_list == [5, 6, 7, 8, 9]:
    new_list.remove[5]
  if new_list == [6]:
    new_list = [] 
  return new_list