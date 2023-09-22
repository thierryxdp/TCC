def filtraMultiplos(l,n):
    t=list[]
    i= 0
    while i<= len(l):
        if (l[i] % n) == 0:
            t = t+(l[i],)
        i+=1    
    return t