def filtraMultiplos(lista,numero):
    indice = 0
    divisiveis = []
    while indice < len(lista):
        if lista[indice]% numero == 0:
            list.append(divisiveis,lista[indice])
            return divisiveis
        indice += 1