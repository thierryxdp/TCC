def filtraMultiplos(lista,n):
    cont = 0 
    divisiveis = []
    while cont < len(lista):
        if (lista[cont])%n == 0:
            divisiveis += [lista[cont]]
        cont = cont + 1
    return divisiveis