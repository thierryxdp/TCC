def filtraMultiplos(lista,n):
    listaMultiplos = []
    i = 0
    k = [n]
    while i < len(lista):
        if lista[i] % k ==0:
        	listaMultiplos = listaMultiplos + lista
        i = i + 1
    return listaMultiplos