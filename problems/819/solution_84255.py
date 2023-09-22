multiplos = []
def filtraMultiplos(x,y):
    for c in x[0][0]:
        if c%y == 0:
            return multiplos.append(c)