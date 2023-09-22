multiplos = []
def filtra(x,y):
    for c in x:
        if c%y == 0:
            return multiplos.append(c)

def filtraMultiplos (x,y):
    return multiplos