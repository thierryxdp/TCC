def filtraMultiplos(lista,num):
    multiplos = []
    while lista > [0,]:
        for x in lista:
            if x%num == 0:
                multiplos.append(x)
                return multiplos