def filtraMultiplos(lista, n):
    multiplo = []
    indice = 0
    while  indice<=(len(lista)-1) :
        if lista[indice]%n==0:
            multiplo= multiplo + [lista[indice]]
        indice = indice + 1
    return multiplo