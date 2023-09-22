def filtraMultiplos(lista,numero):
    indice = 0
    divisiveis = []
    while indice < len(lista):     
        if lista[indice] % numero == 0:
            list.extend(divisiveis,lista[indice])
            return divisiveis
        indice = indice + 1