def filtraMultiplos(lista,n):
    a=lista
    while a<len(lista):
        elemento=lista[index]
        if elemento%n==0:
            return [elemento]
        else:
            return []