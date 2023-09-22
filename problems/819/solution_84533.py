def filtraMultiplos(lista,n):
    tupla=lista[1]
    while tupla<len(lista):
        elemento=lista[tupla]
        if elemento%n==0:
            return [elemento]
        else:
            return []