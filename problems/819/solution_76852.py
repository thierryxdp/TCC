def filtraMultiplos(lista,n):
    listaNew = 0
    i = 0
    k = [lista]
    listaMultiplos = []
    while i < len(k):
        if k[i] % n == 0:
        	listaNew = listaNew + k[i]
        i = i + 1
        listaMultiplos = [listaNew]
    return listaMultiplos