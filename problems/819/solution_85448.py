def filtraMultiplos(lista,n):
    multiplos = []
    for item in lista:
        if item%n==0:
            multiplos.append(item)
    return multiplos