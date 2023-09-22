def filtra_pares(lista):
  for pos,c in enumerate(lista):
    if c%2==1 or c%2==-1:
      del lista[pos]
  lista = tuple(lista[:])
  
  return lista
filtra_pares([1,2,3,4])