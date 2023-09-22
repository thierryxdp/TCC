def filtraMultiplos(lista,n):
    tupla=lista[1,2,3,4,5]
    while tupla<len(lista):
        elemento=lista[tupla]
        if elemento%n==0:
            return [elemento]
        else:
            return []