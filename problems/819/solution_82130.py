def filtraMultiplos(L,M):
    lista = []
    x = 0
    while x <= len(L)+1:
        if L[x] % M == 0:
        lista = lista + L[x]
        elif L[x] % M != 0:
            x = x+1
   return lista