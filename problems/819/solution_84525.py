def filtraMultiplos(lista,n):
    index=lista[0,1,2,3]
    while index< len(lista):
        elemento=lista[index]
        if elemento%n==0:
            return [elemento]
        else:
            return []