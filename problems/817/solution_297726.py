def acima_damedia(notas):
  '''função que dada uma lista com notas, retotna uma lista ordenada com as notas que ficaram acima da media; list->float'''
  m=sum(notas)/len(notas)
  lista=notas+[m]
  list.sort(lista)
  a=list.index(lista,m)
  b=list.count(lista,m)
  return lista[a+b:]