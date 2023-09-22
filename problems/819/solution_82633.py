def filtraMultiplos(lista,n):
    
    pares = []
    i = 0
    while i <len(lista):
        if lista[i]%n == 0:
            pares = pares + [lista[i],]
        i = i + 1
    return pares