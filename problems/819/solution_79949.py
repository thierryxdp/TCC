def filtraMultiplos(x,n):
    multiplos=[]
    i=0
    while i<len(x):
        i=i+1
        if x[i]%n==0:
            multiplos=multiplos+[x[1]]
    return multiplos