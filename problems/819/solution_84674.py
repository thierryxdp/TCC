def filtraMultiplos(lista,numero):
    i = 0
    n = []
    while i<len(lista):
        if lista[i]%numero==0:
            n = n + [lista[i]]
        i = i + 1
    return n