def filtraMultiplos(x,y):
    multiplos = []
    for c in x:
        if c%y == 0:
            return multiplos.append(c)