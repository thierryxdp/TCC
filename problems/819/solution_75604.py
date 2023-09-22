def filtraMultiplos(lista,n):
    multi = []
    i = 0
    while i <len(lista):
        if lista[i]%n == 0:
            multi = multi + [lista[i]]
        i = i + 1
    return multi