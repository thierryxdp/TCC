def filtraMultiplos(lista, n):
    """ """
  
    indice = 0
  
    while lista[indice] % n == 0:
        indice += 1
        lista = lista[indice]
      
    return lista