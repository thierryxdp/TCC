def filtraMultiplos(lista,n):
    i=0
    while i<len(lista):
        if lista[i]%n !=0:
            lista.remove(lista[i])
        else: i=i+1
    return lista