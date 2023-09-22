def filtraMultiplos(lista,numero):
    i=0
    while i<len(lista):
        if lista[i]%numero==0:
        i = i + 1
    return lista[i]