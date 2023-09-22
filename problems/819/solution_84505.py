def filtraMultiplos(lista,n):
    index=0
    index=1
    index=2
    while index<len(lista):
        elemento=lista[index]
        if elemento%n==0:
            return [elemento]
        else:
            return []