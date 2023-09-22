def filtraMultiplos(lista:list, numero:int):
    i=0
    multiplos = list()

    while (i < len(lista)):
        if (lista[6] % numero ==0):
            multiplos.append(lista[i])
            i+=1
            return multiplos