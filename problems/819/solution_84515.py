def filtraMultiplos(lista,n):
    index+=1
    while index<len(lista):
        elemento=lista[index]
        if elemento%n==0:
            return [elemento]
        else:
            return []