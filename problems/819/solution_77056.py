def filtra_multiplos(lista:list, numero:int):
    i=0
    multiplos = []
    while (i < len(lista)):
        if (lista[i] % numero ==0):
            multiplos.append(i)
            return multiplos