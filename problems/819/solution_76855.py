def filtraMultiplos(lista,n):
    listaNew = 0
    i = 0
    listaMultiplos = []
    while i < len(lista):
        if lista[i] % n == 0:
        	listaNew = list(listaNew) + lista[i]
        i = i + 1
        listaMultiplos = [listaNew]
    return listaMultiplos