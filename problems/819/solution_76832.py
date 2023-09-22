def filtraMultiplos(lista,n):
    listaMultiplos = 0
    i = 0
    k = []
    while i < len(lista):
        if lista[i] % n == 0:
        	listaMultiplos = listaMultiplos + lista[i]
            k = [listaMultiplos,]
        i = i + 1
    return k