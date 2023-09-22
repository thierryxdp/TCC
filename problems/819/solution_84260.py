def filtra(x,y):
    multiplos = []
    for c in x:
        if c%y == 0:
            return multiplos.append(c)

def filtraMultiplos (x,y):
    return filtra(x,y)