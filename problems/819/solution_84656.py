def filtraMultiplos(lista, n):
    contador = 0
    divisiveis = []
    while contador<len(lista):
        if lista[contador]%n==0:
            divisiveis = divisiveis + (lista[contador],)
        contador = contador + 1
    return divisiveis