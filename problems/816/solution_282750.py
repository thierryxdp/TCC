def maiores(lista, n):
  lista.sort()
  lista = lista[lista.index(n) + 1 : ]
  return lista