def filtraMultiplos(l,n):
    multiplos = []
    i = 0
    while i <len(l):
        if l[i]%n == 0:
            multiplos = multiplos + [l[i],]
        i = i + 1
    return multiplos