def filtra_multiplos(lista:list, numero:int):
    i=0
    multiplos = list()
    while (i < len(lista)):
        if (lista[i] % numero ==0):
            multiplos.append(lista[i])
            i+=1
    return multiplos