def filtraMultiplos(lista,n):
    while len(lista):
        elemento=lista[index]
        if elemento%n==0:
            return [elemento]
        else:
            return []