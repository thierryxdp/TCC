def filtraMultiplos(ls,n):
    l=[]
    for e in ls:
        if e%n==0:
            l.append(e)
    return l