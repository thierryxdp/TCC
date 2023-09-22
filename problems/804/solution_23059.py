def filtra_pares(t): 
  lista = [] 
  if type(t) == tuple and len(t) == 4:
    for i in t:
      if i%2 == 0:
        lista.append(i)