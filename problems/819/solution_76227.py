def filtraMultiplos(lista, num):
    multiplos = []
    indice = 0

    while indice < len(lista):
        if lista[indice] % num == 0:
            multiplos += [lista[indice]]
            indice += 1
            
        else:
            indice += 1

    return multiplos