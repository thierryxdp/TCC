multiplos = []
def filtraMultiplos(x,y):
    for c in x:
        if c%y == 0:
            return multiplos.append(c)