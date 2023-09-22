def filtraMultiplos(l,n):
    i = 0
    multiplos = 0
    while i%n==0:
        if len(l)==0:
            multiplos = multiplos + 1
            i = i + 1
        else:
            i = i + 1 
    return multiplos