def filtraMultiplos(lista, numero):
    divisiveis = ()
    indice = 0
    while lista[indice] % numero == 0:
        divisiveis = divisiveis + (lista[indice],)
        indice = indice + 1
    return divisiveis