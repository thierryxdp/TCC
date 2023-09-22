def filtraMultiplos(lista,n):
    i = 0
    listaM = []
    while i<len(lista):
        if lista[i]%n == 0:
            listaM = listaM + list(lista[i])
        i = i+1
    return listaM