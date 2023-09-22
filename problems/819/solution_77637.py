def filtraMultiplos(lista,n):
    divisiveis = ()
    positivos = 0
    while positivos >= 0:
        if lista[positivos]/n:
            divisiveis = lista[positivos]