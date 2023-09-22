def filtraMultiplos(lista,n):
    listaMultiplos = []
    i = 0
    while i <= len(lista):
        if len(lista) % n ==0:
        	listaMultiplos = lista + listaMultiplos
        i =+ 1
    return listaMultiplos