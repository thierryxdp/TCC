def filtraMultiplos(lista,n):
    multiplos = []
    for iten in lista:
        if item%n==0:
            multiplos.append(item)
            return multiplos