def filtraMultiplos(lista,n):
    i = 0
    divisiveis = 0
    while i < len(lista):
        if lista[i] %n == 0:
            divisiveis = divisiveis, lista[i]
        i=i+1
    numeros = list(divisiveis)
    return numeros.remove(0)