def filtraMultiplos(lista, numero):
    divisiveis = ()
    indice = 0
    while indice < len(lista):
        if lista[indice] % numero ==0:
           divisiveis = divisiveis + (lista[indice])
           indice = indice + 1
    return divisiveis