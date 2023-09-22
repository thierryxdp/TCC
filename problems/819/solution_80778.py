def filtraMultiplos(lista,n):
    divisiveis = []
    i = 0
    while i < len(lista):
        if lista[i] %n == 0:
            divisiveis = divisiveis + list(lista[i])
        i=i+1
    return divisiveis