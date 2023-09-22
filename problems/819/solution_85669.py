def filtraMultiplos(lista ,numero):
    indice = 0
    multiplos = []
    while indice < len(lista):
        resto = lista[i]%numero
        indice += 1
        if resto == 0:
            multiplos += [lista[indice-1]]
    return multiplos