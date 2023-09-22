def filtra_multiplos(lista,n):
  """ Filtra os multiplos de uma lista por um numero indicado
      lista, int---> return---> lista """
  i=0
  lista2 =[]
  k = len(lista)
  while i<k:
    if (lista[i] % n) == 0:
      list.append(lista2, lista[i])

    i=i+1
  return lista2