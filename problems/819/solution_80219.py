def filtraMultiplos(lista, n):
    y = []
    x = 0
    while x <len(lista):
        if lista[x]%n == 0:
            y = y + [lista[x],]
        x = x + 1
    return y