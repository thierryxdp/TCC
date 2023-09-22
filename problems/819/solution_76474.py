def filtraMultiplos(listaN,n):
    indice = 0
    multiplos = []
    while indice < len(listaN):
        if listaN[indice] % n == 0:
            multiplos.append(listaN[indice])
        indice += 1
    return multiplos