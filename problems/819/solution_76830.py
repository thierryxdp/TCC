def filtraMultiplos(lista,n):
    listaMultiplos = 0
    i = 0
    while i < len(lista):
        if lista[i] % n == 0:
        	listaMultiplos = [listaMultiplos,] + lista[i]
        i = i + 1
    return listaMultiplos