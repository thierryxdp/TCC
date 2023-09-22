def filtraMultiplos(lista,n):
    listaNew = []
    i = 0
    listaMultiplos = []
    while i < len(lista):
        if lista[i] % n == 0:
        	listaNew = [listaNew,lista[i]]
        i = i + 1
        listaMultiplos = [listaNew]
    return listaMultiplos