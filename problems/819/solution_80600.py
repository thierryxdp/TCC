def filtraMultiplos(lista,n):
    i = 0
    listaMultiplos = []
    while i<len(lista):
        if lista[i]%n == 0:
            listaMultiplos + lista[i]
        i = i+1
    return listaMultiplos