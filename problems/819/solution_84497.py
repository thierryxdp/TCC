def filtraMultiplos(lista,n):
    while index<len(lista):
        elemento=lista[index]
        if elemento%n==0:
            return [elemento]
        else:
            return []