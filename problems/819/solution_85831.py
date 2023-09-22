def filtraMultiplos(l,n):
    multiplos=[]
    for i in l:
        if i%n==0:
            multiplos.append(i)
    return multiplos