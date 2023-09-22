def filtra_multiplos(x,y):
    multiplos = []
    for c in x:
        if c%y == 0:
            multiplos.append(c)
    return multiplos