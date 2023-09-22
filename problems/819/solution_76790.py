def filtraMultiplos(lista,n):
    listaMultiplos = []
    i = 0
    while i < len(lista):
        if lista[i] % n ==0:
        	listaMultiplos = lista[i] + listaMultiplos
        i = i + 1
    return listaMultiplos