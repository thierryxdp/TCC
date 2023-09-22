def filtraMultiplos(x,n):
    multiplos=[]
    i=0
    while i < len(x):
        if x[i]%n == 0: 
            multiplos = multiplos + [x[i]]
        i = i + 1    
    return multiplos