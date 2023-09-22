def filtraMultiplos(n, lista):
    lista = []
    contador = 0
    while contador<len(lista):
        if lista[contador]%n==0:
            divisiveis = divisiveis + [lista[contador],]
        contador = contador + 1
    return divisiveis