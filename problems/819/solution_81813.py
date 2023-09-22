def filtraMultiplos(lista,n):
    lista2 = []
    i=0
    while i>len(lista):
      if lista[i] % n == 0:
         lista2.append(lista[i])
      i = i+1
 return lista2