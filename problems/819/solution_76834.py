def filtraMultiplos(lista,n):
    listaMultiplos = 0
    i = 0
    k = []
    while i < len(lista):
        if lista[i] % n == 0:
        	listaMultiplos = listaMultiplos + lista[i]
        i = i + 1
        k = [listaMultiplos,]
    return k