def filtraMultiplos([lista],n):
    i = 0
    divisiveis = []
    while i<len(lista):
        if lista[i]%n == 0:
            divisiveis = divisiveis + [lista[i]]
        i = i + 1
    return divisiveis