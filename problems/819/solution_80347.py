def filtraMultiplos(lista, n):
    i=0
    listad = []
    while i < len(lista): 
        if lista[i]%n == 0: 
            listad = lista[i]
        i=+1 
    return listad